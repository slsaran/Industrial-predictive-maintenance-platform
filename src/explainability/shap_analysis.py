import shap


def create_shap_explainer(model):

    explainer = shap.TreeExplainer(model)

    return explainer


def calculate_shap_values(
    explainer,
    X
):

    shap_values = explainer.shap_values(X)

    return shap_values

import pandas as pd


def get_top_prediction_drivers(
    shap_values,
    feature_values,
    top_n=3
):
    """
    Extract top positive SHAP contributors.
    """

    contribution_df = pd.DataFrame({

        "feature": feature_values.index,

        "feature_value": feature_values.values,

        "shap_value": shap_values

    })

    contribution_df = contribution_df.sort_values(

        by="shap_value",

        ascending=False

    )

    return contribution_df.head(top_n)