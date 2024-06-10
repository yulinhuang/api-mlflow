"""

    
"""

from abc                import ABC, abstractmethod
import mlflow
import os


class AbstractModelConnector(object):
    """

    """

    @abstractmethod
    def get_predictor(self):
        pass

class ModelConnector(AbstractModelConnector):
    """

    """
    def __init__(
            self, 
        ):
        super(ModelConnector, self).__init__()
        

    def get_predictor(
            self,
            model_name: str, model_version: str
        ) -> mlflow.pyfunc.PyFuncModel:
        """
        This function fetches a trained machine learning model from the MLflow
        model registry based on the specified model name and version.

        Args:
            model_name (str): The name of the model to fetch from the model
            registry.
            model_version (str): The version of the model to fetch from the model
            registry.
        Returns:
            model (mlflow.pyfunc.PyFuncModel): The loaded machine learning model.
        Raises:
            Exception: If the model fetching fails, an exception is raised with an
            error message.
        """
        ########## TODO: Setup MLFLOW TRACKING URI and S3 Credential ##########

        model = mlflow.pyfunc.load_model(
            model_uri=f"models:/{model_name}/{model_version}"
        )
        

        return model