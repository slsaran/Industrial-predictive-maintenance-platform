def calculate_risk_score(
    failure_probability
):
    return round(
        float(failure_probability) * 100,
        2
    )


def classify_risk_level(
    failure_probability
):

    if failure_probability < 0.30:
        return "LOW"

    elif failure_probability < 0.70:
        return "MEDIUM"

    return "HIGH"