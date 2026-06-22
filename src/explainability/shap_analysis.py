import shap
import pandas as pd


def create_shap_explainer(model):

    return shap.TreeExplainer(model)


def calculate_shap_values(
    explainer,
    X
):

    return explainer.shap_values(X)


def get_top_drivers(
    model,
    features,
    top_n=3
):

    explainer = create_shap_explainer(
        model
    )

    shap_values = calculate_shap_values(
        explainer,
        features
    )

    contribution_df = pd.DataFrame({

        "feature": features.columns,

        "shap_value": shap_values[0]

    })

    contribution_df["abs_shap"] = (
    contribution_df["shap_value"].abs()
    )

    contribution_df = contribution_df.sort_values(
        by="abs_shap",
        ascending=False
    )

    return contribution_df[
        ["feature", "shap_value"]
    ].head(top_n)