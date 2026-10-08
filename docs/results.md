# Measured results / Labs 01 and 02

Generated from the executed notebook summaries. Seed: 42.

## Lab 01 / Feature engineering

| Features | Validation ROC AUC |
|---|---:|
| raw columns | 0.8421 |
| raw + engineered | 0.8723 |
| engineered + cabin | 0.8677 |
| engineered + fare/family | 0.8721 |
| engineered + both | 0.8679 |

Raw and engineered features use identical row indices and logistic regression.
Additional cabin and fare-per-family features do not improve this split further.

## Lab 01 / Selection

| Model | Validation MAE / grade points |
|---|---:|
| all 30 features | 2.1806 |
| SelectKBest k=5 | 2.1338 |
| SelectKBest k=10 | 2.1385 |
| SelectKBest k=20 | 2.1246 |
| lasso | 2.0773 |
| all 30 + G2 (leakage demo) | 0.7619 |
| also exclude absences | 2.1848 |

Lasso retained 18 of 56 encoded columns.
The G2 row is a deliberate leakage demonstration, not a valid enrolment forecast.
The final row also excludes accumulated absences. All other candidate fields need
a prediction-time availability check for real use.

## Lab 02 / Regression

| Model | Validation MAE | RMSE | R-squared |
|---|---:|---:|---:|
| linear regression | 4181.194 | 5796.285 | 0.7836 |
| ridge | 4238.824 | 5821.592 | 0.7817 |
| bike daily forest | 1040.415 | 1245.024 | 0.5589 |
| bike hourly forest | 56.509 | 84.508 | 0.8531 |

Insurance errors are dollars; bike errors are daily/hourly rentals.
Bike validation contains the last 20% of the series, in time order.

## Lab 02 / Classification

| Model / evaluation | Accuracy | ROC AUC |
|---|---:|---:|
| Titanic logistic / development validation | 0.8204 | 0.8730 |
| Titanic random_forest / development validation | 0.8323 | 0.9093 |
| Titanic tuned logistic / final test | 0.7578 | 0.8374 |
| Heart disease / validation | 0.8826 | 0.9320 |

Titanic baseline accuracy: 0.6168. Best grid: `{'model__C': 0.1, 'model__class_weight': 'balanced'}`.
Mean five-fold CV AUC: 0.8500; 668 development rows and 223 reserved test rows.
The handout reuses one split for Part C and the final test; the worked notebook
reserves the final test before Part C, so its model-comparison results differ.

Breast-cancer validation ROC AUC: 0.9962; average precision: 0.9943.

## Lab 02 / Threshold decision

| Threshold | TN | FP | FN | TP | Precision | Recall |
|---|---:|---:|---:|---:|---:|---:|
| 0.50 | 89 | 1 | 4 | 49 | 0.9800 | 0.9245 |
| 0.30 | 89 | 1 | 2 | 51 | 0.9808 | 0.9623 |

The lower threshold avoids two missed positives with no extra false alerts in this sample.
This is validation evidence for the [coursework decision memo](../results/lab02/decision_memo.md).

## Source evidence

- [Lab 01 summary](../results/lab01/summary.json)
- [Lab 02 summary](../results/lab02/summary.json)
- [Feature comparison](../results/lab01/feature_comparison.csv)
- [Student selection](../results/lab01/student_feature_selection.csv)
- [Insurance metrics](../results/lab02/insurance_metrics.csv)
- [Titanic CV table](../results/lab02/titanic_cv_results.csv)
- [Titanic model card](../models/titanic_survival_card.json)
- [Threshold counts](../results/lab02/cancer_thresholds.csv)
