# Lab 02 / Decision memo

Positive class: malignant. Among the two specified thresholds, choose **0.30** provisionally when missed positives cost more than false alarms.

At 0.50: TN=89, FP=1, FN=4, TP=49; precision=0.980, recall=0.925.

At 0.30: TN=89, FP=1, FN=2, TP=51; precision=0.981, recall=0.962.

Lowering the threshold avoids 2 missed positives and adds 0 false alerts in this validation sample. The probability model is unchanged; only its decision rule changes. An exact optimum requires specified error costs, calibration, and separate evaluation of the chosen threshold. These 143 validation rows support a provisional coursework choice, not deployment.
