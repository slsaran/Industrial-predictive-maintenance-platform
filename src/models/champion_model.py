from xgboost import XGBClassifier


def build_champion_xgboost_model():
    """
    Final production-ready model selected after
    experimentation and hyperparameter tuning.

    Champion Model:
    - max_depth = 4
    - n_estimators = 100
    - learning_rate = 0.1
    - min_child_weight = 1
    - operating threshold = 0.40
    """

    model = XGBClassifier(

        random_state=42,

        max_depth=4,

        n_estimators=100,

        learning_rate=0.1,

        min_child_weight=1,

        objective="binary:logistic",

        eval_metric="logloss"

    )

    return model


CHAMPION_THRESHOLD = 0.40