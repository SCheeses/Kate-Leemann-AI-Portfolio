# Kate Leemann — Applied AI Portfolio

## About Me

I am an Applied AI and Robotics student at Houston Community College with a professional background in genetics research. My interests include computer vision, natural language processing, biological and laboratory applications of machine learning, and responsible evaluation in high-consequence settings.

My research background shapes how I approach technical projects: ask clear questions, document methods, examine errors, and distinguish what the results demonstrate from what still needs testing. I am especially interested in connecting these practices to practical tools for research and laboratory workflows.

This portfolio documents my development through hands-on projects, executed notebooks, saved results, and reflection on model limitations.

## Technical Skills

- **Python and analysis:** Jupyter, Google Colab, NumPy, and Matplotlib
- **Computer vision:** OpenCV, Pillow, PyTorch, TorchVision, YOLO11, and SAM 2
- **Natural language processing:** spaCy, NLTK, text preprocessing, TF-IDF, sentiment analysis, and named entity recognition
- **Machine learning:** Scikit-learn, logistic regression, support vector machines, and multinomial Naive Bayes
- **Evaluation:** Cross-validation, classification reports, confusion matrices, and error analysis
- **Reproducibility:** Git, GitHub, dependency management, validation checks, and technical documentation

## Featured Project: NewsBot Intelligence System

**ITAI 2373 Midterm | Team LeemannTaylor**

I collaborated with Roderick Taylor to develop NewsBot, a natural language processing prototype for news categorization and analysis. We contributed equally and shared responsibilities throughout the project.

The system combines text classification with linguistic analysis to help users explore news articles. Its workflow includes:

- Cleaning and preprocessing article text
- Extracting TF-IDF features and comparing three classification models
- Examining parts of speech, dependency patterns, and candidate semantic roles
- Estimating sentiment and exploratory emotion-keyword cues
- Identifying named entities and visualizing their co-occurrence
- Producing reports, charts, and an integrated dashboard

The corrected notebook achieved **97.57% accuracy** and **0.9740 macro F1** on a 288-article holdout. Because that holdout had already informed earlier error analysis, these results represent a post-submission comparison; independent validation remains future work.

This project reflects my interest in making model behavior understandable through documented methods, visible results, and careful discussion of limitations.

## Repository Organization

The project folder contains the current notebook, datasets, generated results, validation checks, and an archived copy of the original submission. Output folders are summarized below.

~~~text
ITAI2373-NewsBot-Midterm/
├── README.md
├── NewsBot_Intelligence_System.ipynb
├── BBC News Train.csv
├── newsbot_dataset.csv
├── newsbot_processed.csv
├── requirements.txt
├── data_manifest.json
├── .gitattributes
├── .gitignore
├── newsbot_outputs.zip
├── outputs/                       # 39 generated result files
├── public_outputs/                # 37 selected result files
├── tests/
│   └── check_pipeline.py
└── archive/
    └── submitted/
        ├── README.md
        ├── NewsBot_Intelligence_System.ipynb
        ├── BBC News Train.csv
        └── outputs/               # 35 original result files
~~~

- **Main notebook:** The executed, corrected NewsBot workflow.
- **Dataset files:** Source, working, and processed CSV files included in the supplied project folder.
- **`outputs/`:** Model evaluations, predictions, linguistic analyses, visualizations, and demonstration results.
- **`public_outputs/`:** Selected results excluding `test_predictions.csv` and `subject_verb_object_relationships.csv`.
- **`newsbot_outputs.zip`:** A packaged export containing 37 result files.
- **`tests/`:** Checks for the notebook’s pipeline.
- **`archive/submitted/`:** The original submission preserved for comparison.
- **Supporting files:** Dependency requirements, dataset provenance, and Git configuration.

## Reproducibility and Evaluation

I include executed notebooks and saved outputs so readers can examine both the methods and their results. For NewsBot, the project also includes dependency requirements, a dataset manifest, and pipeline validation checks.

I preserve the original submission alongside the corrected version to make changes traceable. I report limitations with the results, including the historical, single-publisher dataset and the need for independent evaluation.

My goal is to build projects that others can inspect, understand, and reproduce while being clear about their intended use and current limits.

## Contact

- **GitHub:** [SCheeses](https://github.com/SCheeses)
- **Portfolio:** [Kate-Leemann-AI-Portfolio](https://github.com/SCheeses/Kate-Leemann-AI-Portfolio)
- **Email:** [kateleemann8@gmail.com](mailto:kateleemann8@gmail.com)
