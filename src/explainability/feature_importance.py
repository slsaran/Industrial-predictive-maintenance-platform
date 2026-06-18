import pandas as pd


def get_feature_importance(model, feature_names):

    importance_df = pd.DataFrame({

        "Feature": feature_names,

        "Importance": model.feature_importances_

    })

    importance_df = importance_df.sort_values(

        by="Importance",

        ascending=False

    )

    return importance_df