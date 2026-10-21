# NewsBot Intelligence System

**ITAI 2373 Midterm | Team LeemannTaylor | Kate Leemann and Roderick Taylor**

[Portfolio repositories](https://github.com/SCheeses/Kate-Leemann-AI-Portfolio) , (https://github.com/RTaylor89/RTaylor89-Roderick_Taylor-AI-Portfolio)

## Status: post-submission correction

The original notebook and its outputs are preserved in [`archive/submitted/`](archive/submitted/). The main notebook contains corrections made after initial run. **The corrected notebook has been executed from start to finish with the supplied BBC CSV.** Both historical and fresh results are reported below.

NewsBot is a prototype for editors and media-monitoring analysts. It suggests a category, finds entity mentions, estimates textual sentiment, and exposes linguistic patterns for human review. It does not establish production readiness or operational time savings.

## Run in Colab or VS Code/Jupyter

1. Obtain `BBC News Train.csv` from the [BBC News Classification competition](https://www.kaggle.com/competitions/learn-ai-bbc/data), accepting its applicable terms. The source data is not redistributed here.
2. Open `NewsBot_Intelligence_System.ipynb`. Put the CSV beside it, in `data/`, or in `/content/` on Colab. Alternatively set the `NEWSBOT_DATASET` environment variable to its absolute path.
3. Run the notebook in order. The setup cell installs pinned core dependencies into the active kernel and downloads `en_core_web_sm` plus NLTK resources. A CPU runtime is sufficient. Restart the kernel if Jupyter requests it after installation, then run all cells.
4. Review the generated metrics and plots in `outputs/`. The last cell creates `newsbot_outputs.zip`, excluding full-article prediction files and extracted source sentences. In Colab it also offers a download.

For an existing local environment:

```sh
python -m pip install -r requirements.txt
python -m spacy download en_core_web_sm
python -m nltk.downloader punkt punkt_tab stopwords wordnet vader_lexicon
python tests/check_pipeline.py
```

Select that same Python environment as the notebook kernel. The model version used for the correction checks is `en_core_web_sm` 3.8.0.

## Dataset and evaluation

The initial run loaded 1,490 labeled BBC articles. Removing 50 exact duplicate texts retained 1,440 articles across Business, Entertainment, Politics, Sports, and Technology. Health is unsupported. A stratified split reserved 288 test articles and 1,152 training articles. Vocabulary fitting occurred within each training fold during three-fold cross-validation.

| Submitted model | Best CV macro F1 |
|---|---:|
| Logistic Regression | 0.9749 |
| Linear-kernel SVM | 0.9746 |
| Multinomial Naive Bayes | 0.9685 |

The initial Logistic Regression model achieved **96.18% accuracy (277/288)** and **0.9598 macro F1**. Technology recall was **87.23%**. These values are historical, not new measurements of the corrected preprocessing. The revised search additionally compares vocabulary limits of 2,000 and 5,000 terms. Because the old test set has already informed error analysis, a new independent dataset is needed for an unbiased assessment of improvements.

### Corrected run

The corrected run selected **SVM** and achieved **97.57% accuracy (281/288)**, **0.9740 macro F1**, and **91.49% Technology recall** on the existing holdout. This is a post-submission regression comparison, not an untouched independent evaluation.

| Model | Revised best CV macro F1 |
|---|---:|
| SVM | 0.9791 |
| Logistic Regression | 0.9726 |
| Naive Bayes | 0.9674 |

SVM explanations report pairwise feature coefficients; these must not be treated as one coefficient row per category.

## Course and assignment alignment

| Assignment component | Course module | Implementation |
|---|---|---|
| 1: Context | 1 | Editorial routing and media monitoring |
| 2: Preprocessing | 2 | HTML decoding, boundaries, contractions, tokenization, stop words, contextual lemmas |
| 3: TF-IDF | 4 | N-grams, TF scaling, vocabulary-size comparison, term plots and coefficients |
| 4: POS | 5 | Article-level proportions and category heatmap |
| 5: Syntax/semantics | 6 | Dependencies, syntactic features, active SVO, candidate passive/active semantic roles |
| 6: Sentiment/emotion | 7 | VADER and normalized exploratory emotion-keyword cues |
| 7: Classification | 8 | Three models, training-only tuning, held-out report, confusion matrix |
| 8: NER | 8 | PERSON, ORG, GPE, DATE, MONEY; frequencies and co-occurrence |

## Corrections and validation

- HTML removal and punctuation now preserve word boundaries; entities and contractions are normalized.
- Contextual spaCy lemmatization replaces noun-only WordNet lemmatization. Classification keeps negation; sentiment, POS, syntax, and NER receive original text.
- Headlines receive sentence-ending punctuation before the body to prevent merged grammatical subjects.
- Candidate semantic roles demonstrate active/passive voice, recipients, and direct negation. A grammatical subject is explicitly not assumed to be a true agent.
- Emotion dictionary entries and article words use the same lemma normalization.
- Inputs with no known TF-IDF vocabulary are rejected rather than receiving an intercept-driven category.
- Local paths, visible warnings, dependency pins, and portable ZIP export replace Colab-only assumptions.
- `tests/check_pipeline.py` tests the notebook's actual definitions with synthetic fixtures. These checks are not accuracy benchmarks.

## Limits and next evaluation

The dataset is historical and single-publisher. Near-duplicate stories may remain. Lowercase source text limits linguistic cues. Unsupported topics still receive a known category unless their vocabulary is entirely unknown. Probability calibration has not been evaluated on independent news. VADER and NER have not been evaluated on human-labeled BBC examples. Emotion cues ignore negation and context. Semantic roles are heuristic candidates, not a trained SRL model; prepositional attachment, instruments, natural forces, pronouns, and quoted claims can be misinterpreted. Entity co-occurrence does not prove a real relationship, and aliases remain unresolved.

The corrected score is measured on the existing holdout; independent validation remains future work.

## Contributions and assistance

Kate Leemann and Roderick Taylor contributed equally and collaboratively with shared responsibilities.

## References

- Instructor-provided NewsBot assignment and `Midterm_NewsBot_Intelligence_System_student.ipynb`.
- ITAI 2373 Modules 2, 4, 5, 6 (Syntax, Parsing, and Semantic Analysis), 7, and 8.
- [BBC News Classification](https://www.kaggle.com/competitions/learn-ai-bbc/data)
- [scikit-learn](https://scikit-learn.org/stable/), [spaCy](https://spacy.io/usage), [NLTK](https://www.nltk.org/)
- [VADER](https://github.com/cjhutto/vaderSentiment), [contractions](https://github.com/kootenpv/contractions)
