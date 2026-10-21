"""Focused regression checks against the notebook's actual function definitions.
Run from the project folder: python tests/check_pipeline.py
Requires requirements.txt, en_core_web_sm, and the listed NLTK resources.
These synthetic fixtures test behavior, not generalization accuracy.
"""
import ast
import json
from pathlib import Path
import re
import html
import unicodedata
from html.parser import HTMLParser
from collections import Counter
import contractions
import numpy as np
import pandas as pd
import spacy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

project = Path(__file__).resolve().parents[1]
nb = json.loads((project / 'NewsBot_Intelligence_System.ipynb').read_text())
ns = dict(globals(), nlp=spacy.load('en_core_web_sm'), sia=SentimentIntensityAnalyzer())
ns['stop_words'] = set(stopwords.words('english')) - {'no', 'not', 'nor'}
ns['required_entity_types'] = {'PERSON', 'ORG', 'GPE', 'DATE', 'MONEY'}
ns['emotion_lexicon'] = {'joy': {'celebrate', 'happy'}, 'fear': {'fear'}}
for cell in nb['cells']:
    if cell['cell_type'] != 'code':
        continue
    source = ''.join(cell['source'])
    if source.startswith('# Install'):
        continue
    tree = ast.parse(source)
    definitions = [x for x in tree.body if isinstance(x, (ast.ClassDef, ast.FunctionDef))]
    exec(compile(ast.Module(body=definitions, type_ignores=[]), 'notebook', 'exec'), ns)

checks = []
def check(name, result):
    assert result, name
    checks.append(name)

clean = ns['clean_text']; preprocess = ns['preprocess_text']; nlp = ns['nlp']
check('hyphen boundaries', clean('state-of-the-art technology') == 'state of the art technology')
check('HTML entities', clean('profit &amp; growth') == 'profit growth')
check('HTML block boundaries', clean('<p>first</p><p>second</p>') == 'first second')
check('script contents excluded', clean('<script>alert(1)</script>News') == 'news')
check('curly apostrophes and contractions', 'not' in clean("This isn’t good; don't buy"))
check('missing input', clean(None) == '' and preprocess('') == '')
check('contextual verb lemmatization', 'run' in preprocess('The athletes were running.').split())
check('negation preserved', 'not' in preprocess('The product is not good.').split())
roles = ns['extract_semantic_roles'](nlp('The startup was acquired by the company.'))
check('passive roles', any(r['candidate_agent'] == ['the company'] and r['candidate_patient'] == ['The startup'] for r in roles))
roles = ns['extract_semantic_roles'](nlp('The company did not acquire the startup.'))
check('negated relationship', any(r['negated'] for r in roles))
roles = ns['extract_semantic_roles'](nlp('The detective gave the evidence to the lawyer.'))
check('recipient role', any('the lawyer' in r['candidate_recipient'] for r in roles))
check('empty sentiment unavailable', ns['analyze_sentiment']('')['sentiment_label'] == 'unavailable')
check('NER required types', all(e['label'] in ns['required_entity_types'] for e in ns['entities_from_doc'](nlp('Maya Chen works in Boston.'))))

# Fit only a small functional fixture; these scores are never reported as project accuracy.
texts = ['football team won the match', 'players scored goals at the stadium',
         'computer software protects the network', 'security software updates computer devices']
model = Pipeline([('tfidf', TfidfVectorizer()), ('classifier', LogisticRegression())])
model.fit([preprocess(t) for t in texts], ['Sports','Sports','Technology','Technology'])
bot = ns['NewsBotIntelligenceSystem'](model, nlp)
result = bot.process_article('Football club celebrates championship victory',
    'London football club Riverside United won the match. Daniel Reed scored two goals.')
check('headline boundary', not any('\n' in row['subject'] for row in result['candidate_relationships']))
check('integrated components', all(k in result for k in ['entities','sentiment','candidate_semantic_roles','pos_proportions','top_tfidf_terms']))
check('JSON serialization', bool(json.dumps(result)))
for name, text in [('empty content',''), ('all unknown vocabulary','zzzxxyqq qqqzzzxxx')]:
    try:
        bot.process_article('', text)
    except ValueError:
        check(name, True)
    else:
        check(name, False)

print(f'{len(checks)} regression checks passed.')
for name in checks:
    print('PASS:', name)
