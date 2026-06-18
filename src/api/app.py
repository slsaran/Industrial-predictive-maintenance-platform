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

    report = create_prediction_report(

        probability

    )

    return report