from pathlib import Path
import pandas as pd

def load_ai4i_dataset() -> pd.DataFrame:
    """
    Load AI4I predictive maintenance dataset.

    Returns
    -------
    pd.DataFrame
        Loaded Dataset.
    """
    project_root = Path(__file__).resolve().parents[2]

    dataset_path= (
        project_root
        / "data"
        / "raw"
        / "ai4i2020.csv"
    )

    if not dataset_path.exists():
        raise FileNotFoundError(
            f"Dataset not found: {dataset_path}"
        )
    df=pd.read_csv(dataset_path)
    return df