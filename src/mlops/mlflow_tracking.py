import mlflow


def start_experiment(
    experiment_name
):

    mlflow.set_experiment(
        experiment_name
    )

    return mlflow.start_run()


def log_model_metrics(
    metrics
):

    for key, value in metrics.items():

        mlflow.log_metric(
            key,
            value
        )


def log_model_params(
    params
):

    for key, value in params.items():

        mlflow.log_param(
            key,
            value
        )