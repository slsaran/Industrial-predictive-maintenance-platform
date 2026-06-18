import pandas as pd


FEATURE_ORDER = [

    "air_temperature_k",
    "process_temperature_k",
    "rotational_speed_rpm",
    "torque_nm",
    "tool_wear_min",

    "temperature_difference",
    "power_proxy",
    "mechanical_stress_index",
    "thermal_stress_index",

    "Type_H",
    "Type_L",
    "Type_M"
]


def create_features(input_data):

    df = pd.DataFrame([input_data])

    df["temperature_difference"] = (

        df["process_temperature_k"]

        -

        df["air_temperature_k"]

    )

    df["power_proxy"] = (

        df["rotational_speed_rpm"]

        *

        df["torque_nm"]

    )

    df["mechanical_stress_index"] = (

        df["torque_nm"]

        /

        df["rotational_speed_rpm"]

    )

    df["thermal_stress_index"] = (

        df["tool_wear_min"]

        *

        df["temperature_difference"]

    )

    df.rename(
        columns={
            "type_h": "Type_H",
            "type_l": "Type_L",
            "type_m": "Type_M"
        },
        inplace=True
    )

    return df[FEATURE_ORDER]