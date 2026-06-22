from src.scoring.risk_scoring import (
    classify_risk_level
)

def test_low_risk():

    assert classify_risk_level(
        0.1
    ) == "LOW"


def test_medium_risk():

    assert classify_risk_level(
        0.5
    ) == "MEDIUM"


def test_high_risk():

    assert classify_risk_level(
        0.9
    ) == "HIGH"