"""Use the Titanic pipeline saved by Lab 02, without retraining.

Example: python predict_passenger.py --pclass 2 --sex female --age 30 --fare 20
"""
import argparse
import json
import math
from pathlib import Path

import joblib
import pandas as pd
import sklearn

MODELS = Path(__file__).resolve().parent / "models"


def nonnegative_float(text):
    value = float(text)
    if not math.isfinite(value) or value < 0:
        raise argparse.ArgumentTypeError("must be a finite nonnegative number")
    return value


def nonnegative_int(text):
    value = int(text)
    if value < 0:
        raise argparse.ArgumentTypeError("must be a nonnegative integer")
    return value


def main():
    parser = argparse.ArgumentParser(description="Predict survival using the Lab 02 model.")
    parser.add_argument("--pclass", type=int, required=True, choices=[1, 2, 3])
    parser.add_argument("--sex", required=True, choices=["male", "female"])
    parser.add_argument("--age", type=nonnegative_float, required=True)
    parser.add_argument("--fare", type=nonnegative_float, required=True)
    parser.add_argument("--sibsp", type=nonnegative_int, default=0)
    parser.add_argument("--parch", type=nonnegative_int, default=0)
    parser.add_argument("--embarked", default="S", choices=["C", "Q", "S"])
    args = parser.parse_args()
    model_path = MODELS / "titanic_survival.joblib"
    card_path = MODELS / "titanic_survival_card.json"
    if not model_path.is_file() or not card_path.is_file():
        parser.error("Saved model missing. Run Lab 02 or: python scripts/run_labs.py --lab 02")
    card = json.loads(card_path.read_text(encoding="utf-8"))
    if card["scikit_learn_version"] != sklearn.__version__:
        parser.error("Package version differs from the model card. Install requirements.txt or rerun Lab 02.")
    model = joblib.load(model_path)
    passenger = pd.DataFrame([{
        "Pclass": args.pclass, "Sex": args.sex, "Age": args.age,
        "SibSp": args.sibsp, "Parch": args.parch, "Fare": args.fare, "Embarked": args.embarked,
    }])[card["features"]]
    probability = float(model.predict_proba(passenger)[0, list(model.classes_).index(1)])
    decision = "survived" if probability >= card["decision_threshold"] else "did not survive"
    print(f"survival probability: {probability:.3f}  ->  {decision}")
    print(f"(model: {card['model']}, test ROC AUC {card['final_test_roc_auc']})")


if __name__ == "__main__":
    main()
