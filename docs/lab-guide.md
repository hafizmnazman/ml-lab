# What to study in the worked notebooks

## Lab 01

Read the markdown above each cell, run it, and compare its output with the
interpretation. Part A records versions and inspects passenger data. Part B
adds family size, isolation, title, and log fare and holds the model and split
fixed. It also compares cabin initial and fare per family member. Part C shows
the same five tumours with raw and standardized distances. Part D compares
ridge, SelectKBest with k=5/10/20, lasso, and an intentionally leaky grade.
The final cell answers all three understanding questions.

The student comparison follows the handout's 30 candidates. A separate
sensitivity run removes accumulated absences because their availability at
enrolment is questionable. Selected coefficients are associations, not causes.

## Lab 02

Part A compares OLS and ridge on medical charges and inspects residuals.
The smoker effect is interpreted as the difference between the two encoded
category coefficients. Part B fits daily and hourly demand models using the
first 80% for training and the last 20% for validation. Full-day observed weather
is a conditional input; earlier forecasts would require weather forecasts or
lagged inputs.

Part C compares passenger classifiers and thresholds, then explains the
breast-cancer confusion matrices, ROC curve, and precision-recall curve.
The memo uses observed false negatives and false positives to justify a
provisional 0.30 threshold. Part D tunes logistic regression with five-fold
cross-validation, and Part E saves and reloads the complete pipelines.
The heart-disease extension, all three lab questions, and the Chapter 4
questions are included at the end.

The Titanic final test is reserved **before** the Part C comparison and used
only for the final evaluation. This corrects the handout's reuse of one split
for both validation and final testing. Part C metrics therefore differ from
the handout's example even with the same seed.

## How to read the evidence

Higher ROC AUC means better positive/negative ranking. Higher accuracy means
more correct thresholded decisions; compare it with the majority baseline.
Lower MAE means smaller average absolute prediction error, in target units.
Threshold selection affects the confusion matrix without changing the fitted
probabilities. The [results report](results.md) links the measured tables.

Preprocessing, feature selection, and model fitting belong in training
pipelines. See the [scikit-learn pipeline documentation](https://scikit-learn.org/stable/modules/compose.html).
