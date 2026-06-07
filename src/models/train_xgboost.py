from xgboost import XGBClassifier

def build_xgboost_model():
    """
    Build baseline XGBoost classifier
    """

    model = XGBClassifier(
        random_state=42,
        n_estimators=100,
        max_depth=4,
        learning_rate=0.1,
        objective="binary:logistic",
        eval_metric="logloss"
    )

    return model

from xgboost import XGBClassifier


def build_balanced_xgboost_model():
    """
    Build imbalance-aware XGBoost classifier.
    """

    model = XGBClassifier(

        random_state=42,

        n_estimators=100,

        max_depth=4,

        learning_rate=0.1,

        objective="binary:logistic",

        eval_metric="logloss",

        scale_pos_weight=9661 / 339

    )

    return model

def build_tuned_xgboost_model(
    max_depth=4,
    n_estimators=100,
    learning_rate=0.1,
    min_child_weight=1
):
    """
    Build configurable XGBoost model for
    hyperparameter tuning experiments.
    """

    model = XGBClassifier(

        random_state=42,

        max_depth=max_depth,

        n_estimators=n_estimators,

        learning_rate=learning_rate,

        min_child_weight=min_child_weight,

        objective="binary:logistic",

        eval_metric="logloss"

    )

    return model