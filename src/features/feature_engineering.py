import pandas as pd


def create_engineered_features(
    df: pd.DataFrame
) -> pd.DataFrame:
    """
    Create engineered features for predictive maintenance.

    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe.

    Returns
    -------
    pd.DataFrame
        Dataframe with engineered features.
    """

    df = df.copy()

    df["Temperature Difference"] = (
        df["Process temperature [K]"]
        - df["Air temperature [K]"]
    )

    df["Power Proxy"] = (
        df["Rotational speed [rpm]"]
        * df["Torque [Nm]"]
    )

    df["Mechanical Stress Index"] = (
        df["Torque [Nm]"]
        / df["Rotational speed [rpm]"]
    )

    df["Thermal Stress Index"] = (
        df["Temperature Difference"]
        * df["Torque [Nm]"]
    )

    return df