from src.scoring.risk_scoring import (
    calculate_risk_score,
    classify_risk_level
)


def create_prediction_report(
    failure_probability
):
    """
    Generate prediction report.
    """

    report = {

        "failure_probability":
        round(
            float(failure_probability),
            4
        ),

        "risk_score":
        float(
            calculate_risk_score(
                failure_probability
            )
        ),

        "risk_level":
        classify_risk_level(
            failure_probability
        )
    }

    return report