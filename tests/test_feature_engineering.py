import pandas as pd

from src.features.feature_engineering import (
    create_engineered_features
)


def test_create_engineered_features():

    df = pd.DataFrame({

        "Air temperature [K]": [300],

        "Process temperature [K]": [310],

        "Rotational speed [rpm]": [1000],

        "Torque [Nm]": [50]

    })

    result = create_engineered_features(df)

    assert result["Temperature Difference"].iloc[0] == 10

    assert result["Power Proxy"].iloc[0] == 50000

    assert result["Mechanical Stress Index"].iloc[0] == 0.05

    assert result["Thermal Stress Index"].iloc[0] == 500