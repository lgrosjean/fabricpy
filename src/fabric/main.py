import pandas as pd

from fabric.semantic_model import SemanticModel
from fabric.workspace import Workspace


def list_datasets(workspace_name: str) -> pd.DataFrame:
    """List all datasets in a workspace."""
    return Workspace(workspace_name).get_datasets()


def get_semantic_model(workspace_name: str, dataset_name: str) -> SemanticModel:
    """Get a dataset from a workspace."""
    return SemanticModel(workspace_name, dataset_name)
