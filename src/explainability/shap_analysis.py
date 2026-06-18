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