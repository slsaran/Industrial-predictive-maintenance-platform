import pandas as pd


def prepare_modeling_dataset(
    df: pd.DataFrame
):
    """
    Prepare dataset for model training.
    """

    df = df.copy()

    df = df.drop(
        columns=[
            "UDI",
            "Product ID",
            "TWF",
            "HDF",
            "PWF",
            "OSF",
            "RNF"
        ]
    )

    df = pd.get_dummies(
        df,
        columns=["Type"],
        drop_first=False
    )

    dummy_columns = [
        "Type_H",
        "Type_L",
        "Type_M"
    ]

    df[dummy_columns] = (
        df[dummy_columns]
        .astype(int)
    )
    df = df.rename(
    columns={
        "Air temperature [K]":
            "air_temperature_k",

        "Process temperature [K]":
            "process_temperature_k",

        "Rotational speed [rpm]":
            "rotational_speed_rpm",

        "Torque [Nm]":
            "torque_nm",

        "Tool wear [min]":
            "tool_wear_min",

        "Temperature Difference":
            "temperature_difference",

        "Power Proxy":
            "power_proxy",

        "Mechanical Stress Index":
            "mechanical_stress_index",

        "Thermal Stress Index":
            "thermal_stress_index"
    }
)

    return df