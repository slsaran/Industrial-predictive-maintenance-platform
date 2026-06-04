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

    return df