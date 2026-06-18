from pathlib import Path

import joblib


from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

MODEL_DIR = PROJECT_ROOT / "models"

MODEL_DIR.mkdir(
    exist_ok=True
)

def save_model(
    model,
    model_name
):

    model_path = MODEL_DIR / f"{model_name}.joblib"

    joblib.dump(
        model,
        model_path
    )

    return model_path


def load_model(
    model_name
):

    model_path = MODEL_DIR / f"{model_name}.joblib"

    return joblib.load(
        model_path
    )