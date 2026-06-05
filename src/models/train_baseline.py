from sklearn.linear_model import LogisticRegression

def build_baseline_model():
    """
    Create baseline logistic regression model.
    """

    model = LogisticRegression(
        max_iter=1000,
        random_state=42
    )
    return model

def build_balanced_model():

    model = LogisticRegression(
        class_weight="balanced",
        max_iter=1000,
        random_state=42
    )

    return model