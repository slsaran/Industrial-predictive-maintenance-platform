from fastapi import FastAPI

from src.api.schemas import (
    MachineInput,
    PredictionResponse
)

from src.models.model_registry import (
    load_model
)

from src.pipeline.inference_pipeline import (
    create_features
)

from src.scoring.prediction_report import (
    create_prediction_report
)
from src.explainability.shap_analysis import (
    get_top_drivers
)

app = FastAPI()

model = load_model(
    "champion_model"
)


@app.get("/")
def home():

    return {

        "message":
        "Industrial Predictive Maintenance API"

    }


@app.post(
    "/predict",
    response_model=PredictionResponse
)
def predict(
    machine: MachineInput
):

    features = create_features(

        machine.model_dump()

    )

    probability = model.predict_proba(

        features

    )[0][1]

    drivers_df = get_top_drivers(
    model,
    features,
    top_n=3
    )

    top_drivers = drivers_df[
        "feature"
    ].tolist()

    report = create_prediction_report(

        probability,

        top_drivers

    )

    return report