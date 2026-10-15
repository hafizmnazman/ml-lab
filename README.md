<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset=".github/readme/banner-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset=".github/readme/banner-light.svg">
    <img src=".github/readme/banner-dark.svg" alt="ML-LAB" width="850">
  </picture>
</div>

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset=".github/readme/card-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset=".github/readme/card-light.svg">
    <img src=".github/readme/card-dark.svg" alt="ML-LAB, worked notebooks for UTP's TEB3123 Machine Learning: three of eight labs done, covering feature engineering and selection, the supervised workflow and the main model families, with a breast cancer SVM at 0.997 test ROC AUC" width="850">
  </picture>
</div>

<p align="center">
  <a href="#hafizml-lab-ls-all_experiments"><img src="https://img.shields.io/badge/labs-3_of_8_done-79e0b0?style=for-the-badge&labelColor=161b22" alt="labs: 3 of 8 done"></a>
  <a href="#hafizml-lab-cat-resultssummaryjson"><img src="https://img.shields.io/badge/titanic-0.837_test_roc_auc-c9f7e0?style=for-the-badge&labelColor=161b22" alt="titanic: 0.837 test ROC AUC"></a>
  <a href="#hafizml-lab-python--m-venv-venv"><img src="https://img.shields.io/badge/python-3.12_%C2%B7_scikit--learn_1.9-3fb950?style=for-the-badge&labelColor=161b22" alt="python 3.12, scikit-learn 1.9"></a>
</p>

```text
hafiz@ml-lab:~$ cat ./about
worked notebooks for teb3123 machine learning at utp, one per lab. each one
follows its handout part by part, does the try-it exercises, answers the
questions, and saves every chart and table it draws.

hafiz@ml-lab:~$ cd all_experiments
hafiz@ml-lab:~/all_experiments$ python predict_passenger.py --pclass 2 --sex female --age 30 --fare 20
survival probability: 0.805  ->  survived
(model: logistic regression pipeline, test ROC AUC 0.837)
```

### <samp>hafiz@ml-lab:~$ jupyter lab</samp>

<p align="center">
  <img src=".github/readme/shots/jupyterlab.png" alt="JupyterLab with the Lab 2 notebook open on the hourly bike demand cell: the code, actual and predicted rentals for the first validation week, and the observations underneath" width="850">
</p>

Each part opens with a short note on what it does and closes with an **Observations** cell that
says what the numbers show. Above is Lab 2, Part B: the forest picks up the two commuter peaks of
a working day and misses a rainy Friday morning.

### <samp>hafiz@ml-lab:~$ ls all_experiments/</samp>

| lab | notebook | topic | datasets | status |
|:--|:--|:--|:--|:--|
| 01 | [`lab01_features_worked`](all_experiments/lab01_features_worked.ipynb) | Feature engineering and selection | Titanic, breast cancer, student performance | done |
| 02 | [`lab02_supervised_workflow_worked`](all_experiments/lab02_supervised_workflow_worked.ipynb) | Regression, classification, the workflow | Insurance, bike sharing, Titanic, breast cancer, heart disease | done |
| 03 | [`lab03_supervised_models_worked`](all_experiments/lab03_supervised_models_worked.ipynb) | KNN, naive Bayes, trees, ensembles, SVMs | Breast cancer, Titanic, Ames housing, red wine | done |
| 04 | `lab04_clustering_pca_worked` | K-means, DBSCAN, PCA | Mall customers, digits | next |
| 05 | `lab05_anomaly_limited_labels_worked` | Anomaly detection, limited labels | Credit card fraud, breast cancer | |
| 06 | `lab06_reinforcement_worked` | Reinforcement learning | | |
| 07 | `lab07_deep_learning_cnn_worked` | CNNs | Digits | |
| 08 | `lab08_deep_learning_lstm_worked` | LSTM forecasting | Bike sharing | |

[`predict_passenger.py`](all_experiments/predict_passenger.py) sits next to the notebooks and
loads the model Lab 2 saves, without retraining.

### <samp>hafiz@ml-lab:~$ cat ./marking-guide</samp>

Where each handout task lives. Every notebook is committed with its outputs, so GitHub shows
every result without running anything.

| lab | the handout asks for | where it is |
|:--|:--|:--|
| 01 | Parts A to D | the Part A to Part D sections, each closing with Observations |
| 01 | Try it yourself: cabin initial and fare per family member | Part B, under *Try it yourself* |
| 01 | Try it yourself: SelectKBest with k=5 and k=20 | Part D, next to k=10 |
| 01 | Check your understanding (3 questions) | the last section |
| 02 | Parts A to E | the Part A to Part E sections |
| 02 | Decision memo | the end of Part C, after the ROC and PR curves |
| 02 | Run `predict_passenger.py` from the terminal | Part E, with its output; the script is in `all_experiments/` |
| 02 | Try it yourself: heart disease | the section after Part E |
| 02 | Check your understanding (3 questions), plus Chapter 4's | the last two sections |
| 03 | Parts A to D | the Part A to Part D sections, each closing with Observations |
| 03 | Save, reload and check `models/breast_cancer_svm.joblib` | the end of Part D |
| 03 | Try it yourself: unpruned tree, linear-only SVM search | the *Try it yourself* section after Part D |
| 03 | Verification checklist | the section after *Try it yourself* |
| 03 | Check your understanding (3 questions) | the last section |

### <samp>hafiz@ml-lab:~$ open results/lab01/</samp>

<table>
  <tr>
    <td width="50%"><samp>same model, same split, new features</samp></td>
    <td width="50%"><samp>same five tumours, two geometries</samp></td>
  </tr>
  <tr>
    <td><img src="results/lab01/titanic_feature_comparison.png" alt="Validation ROC AUC for five Titanic feature sets on one split: raw columns 0.842, engineered 0.872, plus cabin 0.868, plus fare per family 0.872, plus both 0.868"></td>
    <td><img src="results/lab01/scaling_geometry.png" alt="Distance heatmaps between the first five tumours, in raw units and after standardizing"></td>
  </tr>
  <tr>
    <td>Family size, title and log fare lift Titanic validation ROC AUC from 0.842 to 0.872. The deck letter and fare per family member add nothing on top.</td>
    <td>Raw distances are almost pure tumour area. After standardizing, tumour 5's nearest neighbour changes from tumour 3 to tumour 2.</td>
  </tr>
</table>

<p align="center">
  <img src="results/lab01/student_selection.png" alt="Validation MAE for predicting final grades: all 30 features 2.18, SelectKBest 2.12 to 2.14, lasso 2.08, and 0.76 once the leaked G2 grade is added; next to it, the lasso's nonzero coefficients" width="850">
</p>

Predicting final grades at enrolment: ten columns do as well as thirty (MAE 2.14 against 2.18),
and lasso does best at 2.08 with 16 columns. The orange bar is the trap. Add the second-period
grade `G2` and the error drops to 0.76, a score nobody can get on enrolment day.

### <samp>hafiz@ml-lab:~$ open results/lab02/</samp>

<table>
  <tr>
    <td width="50%"><samp>two models, two metrics, two winners</samp></td>
    <td width="50%"><samp>one model, two thresholds</samp></td>
  </tr>
  <tr>
    <td><img src="results/lab02/titanic_baselines.png" alt="Titanic validation accuracy and ROC AUC for logistic regression and a random forest, against the majority baseline"></td>
    <td><img src="results/lab02/cancer_confusion_matrices.png" alt="Breast cancer confusion matrices at thresholds 0.50 and 0.30"></td>
  </tr>
  <tr>
    <td>The random forest wins on accuracy (0.798 against 0.776) and logistic regression on ROC AUC (0.842 against 0.834). Gaps this small need cross-validation to call.</td>
    <td>Lowering the threshold from 0.50 to 0.30 catches two more malignant tumours (missed ones drop from 4 to 2) and adds no false alarm.</td>
  </tr>
  <tr>
    <td><samp>the smoker bands</samp></td>
    <td><samp>the folds disagree more than the settings</samp></td>
  </tr>
  <tr>
    <td><img src="results/lab02/insurance_residuals.png" alt="Ridge regression on insurance charges: actual against predicted, and residuals, with smokers in orange"></td>
    <td><img src="results/lab02/titanic_cross_validation.png" alt="Cross-validated ROC AUC with fold standard deviations for each C and class weight"></td>
  </tr>
  <tr>
    <td>Smokers split into two residual bands: lean smokers come out about $9,000 too high, smokers with a BMI of 30 or more about $7,500 too low. A linear model without an interaction term cannot fix that.</td>
    <td>All ten settings of C and class weight score between 0.847 and 0.850, inside a fold to fold spread of about 0.02. The pick (C=0.1, balanced) tests at 0.837.</td>
  </tr>
</table>

### <samp>hafiz@ml-lab:~$ open results/lab03/</samp>

<p align="center">
  <img src="results/lab03/cancer_decision_boundaries.png" alt="Decision regions on tumour radius and texture for logistic regression (0.88 accuracy), KNN with k=11 (0.90) and Gaussian naive Bayes (0.86), with the validation tumours plotted on top" width="850">
</p>

Same two features, three model families: logistic regression draws a straight line, naive Bayes
a curve, and KNN a ragged edge that follows local votes. On all 30 features KNN wins on accuracy
(0.958) and naive Bayes on ROC AUC (0.992), so the metrics disagree on the winner, as they did
for Titanic in Lab 2.

<table>
  <tr>
    <td width="50%"><samp>deeper trees memorise</samp></td>
    <td width="50%"><samp>is the gap bigger than the spread?</samp></td>
  </tr>
  <tr>
    <td><img src="results/lab03/titanic_tree_depth.png" alt="Titanic decision tree accuracy for max_depth 1 to 12: training rises to 0.954 while validation peaks at depth 3 with 0.785"></td>
    <td><img src="results/lab03/ames_cv_folds.png" alt="Ames Housing log-RMSE on each of three folds for a random forest and gradient boosting, with the fold means"></td>
  </tr>
  <tr>
    <td>Training accuracy climbs to 0.954 at depth 12 while validation peaks at depth 3 (0.785). Left unpruned, the tree hits 0.978 on training rows and drops to 0.722 on validation.</td>
    <td>Boosting beats the forest on every Ames fold (log-RMSE 0.127 against 0.138), but the folds swing by more than the gap. On red wine the forest wins instead.</td>
  </tr>
</table>

### <samp>hafiz@ml-lab:~$ cat results/*/summary.json</samp>

| lab | experiment | result |
|:--|:--|:--|
| 01 | Titanic, raw columns against engineered features | validation ROC AUC 0.842 → 0.872 |
| 01 | Student grades at enrolment, lasso | MAE 2.08 grade points, 16 of 56 columns kept |
| 02 | Insurance charges, OLS | MAE $4,181, R² 0.784 |
| 02 | Daily bike rentals, random forest | MAE 1,040 a day (average day 5,898) |
| 02 | Hourly bike rentals, random forest | MAE 56.5 an hour (average hour 249) |
| 02 | Titanic, logistic regression tuned by 5-fold CV | CV ROC AUC 0.850, test 0.837 |
| 02 | Breast cancer, threshold 0.50 → 0.30 | recall 0.925 → 0.962, precision 0.98 at both |
| 02 | Heart disease (try it yourself) | accuracy 0.883, ROC AUC 0.932 |
| 03 | Breast cancer, KNN (k=11) against Gaussian naive Bayes | accuracy 0.958 against 0.944, ROC AUC 0.986 against 0.992 |
| 03 | Titanic decision tree, depth 1 to 12 | validation peaks at depth 3 (0.785), unpruned tree 0.722 |
| 03 | Ames log price, boosting against forest (3-fold CV) | log-RMSE 0.127 against 0.138 |
| 03 | Red wine quality, forest against boosting | MAE 0.432 against 0.476 |
| 03 | Breast cancer SVM, RBF tuned by 5-fold CV | CV ROC AUC 0.995, test 0.997 (a linear kernel ties at 0.997) |

The decision memo for the cancer threshold closes Part C of
[Lab 2](all_experiments/lab02_supervised_workflow_worked.ipynb).

### <samp>hafiz@ml-lab:~$ python -m venv .venv</samp>

Route A from the course setup chapter, on Windows with Python 3.12:

```powershell
git clone https://github.com/hafizmnazman/ml-lab.git
cd ml-lab
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
jupyter lab all_experiments
```

On macOS or Linux, create it with `python3 -m venv .venv` and activate it with
`source .venv/bin/activate`. Open a notebook and choose **Run > Run All Cells**. In VS Code, open
the notebook, pick the `.venv` interpreter as the kernel and press **Run All**. Both start the
notebook inside `all_experiments/`, which is where the code expects to run.

### <samp>hafiz@ml-lab:~$ tree -L 2</samp>

```text
all_datasets/        the 12 course datasets, unchanged (the digits zip stays zipped for lab 4)
all_experiments/     one worked notebook per lab, plus predict_passenger.py
models/              the pipelines labs 2 and 3 save, and the titanic model card
results/labNN/       charts, tables and summary.json, one folder per lab notebook
requirements.txt     the course packages, pinned to the versions the notebooks ran with
course_materials/    the lecturer's handouts, kept on this machine only (gitignored)
.github/readme/      the banner, the card and the screenshot on this page
```

The layout follows the course setup chapter, so each new lab adds one
`labNN_..._worked.ipynb` and one `results/labNN/`.

### <samp>hafiz@ml-lab:~$ cat ./notes</samp>

- Part D of Lab 2 and of Lab 3 each reuse a split from earlier in the lab (Part C and Part A),
  as the handouts do, so those test rows had already been scored once. The tuning never sees
  them, but strictly they are not fresh. Each notebook says so where it happens.
- In Lab 1 the handout's `coef_ != 0` count says lasso kept 18 columns. Two of those
  coefficients are around 1e-15, floating-point noise from one-hot pairs that always sum to 1,
  so 16 is the real count.
- The numbers on this page come from one run with `random_state=42` on the pinned versions.
  Other package versions can move the last decimal.

### <samp>hafiz@ml-lab:~$ cat ./credits</samp>

The datasets are the course's copies of these Kaggle datasets, and each source page lists its
licence: [Titanic](https://www.kaggle.com/datasets/yasserh/titanic-dataset),
[Breast Cancer Wisconsin](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data),
[Student Performance](https://www.kaggle.com/datasets/larsen0966/student-performance-data-set),
[Medical Cost Personal](https://www.kaggle.com/datasets/mirichoi0218/insurance),
[Bike Sharing](https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset),
[Heart Failure Prediction](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction),
[Ames Housing](https://www.kaggle.com/datasets/shashanknecrothapa/ames-housing-dataset),
[Red Wine Quality](https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009),
[Mall Customers](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python),
[Optical Recognition of Handwritten Digits](https://www.kaggle.com/datasets/yadavhim/optical-recognition-of-handwritten-digits)
and [Credit Card Fraud Detection](https://www.kaggle.com/datasets/miadul/credit-card-fraud-detection-dataset).
The lab handouts belong to the course and stay out of this repo.

<sub>The banner and card are generated by <code>.github/readme/build.py</code> (standard library Python). Change a value at the top and run it again.</sub>
