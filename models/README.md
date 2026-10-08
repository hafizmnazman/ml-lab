# Saved pipelines

Lab 02 generates `titanic_survival.joblib` and `insurance_charges.joblib` here,
together with JSON model cards. The binary pipelines remain local; the cards
are committed as execution evidence. Recreate the pipelines by running:

```powershell
.\.venv\Scripts\python.exe scripts\run_labs.py --lab 02
```

`predict_passenger.py` uses the saved Titanic pipeline. Only load trusted
joblib files and use the package versions recorded in the corresponding card.
