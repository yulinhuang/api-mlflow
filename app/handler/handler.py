"""
    
    
"""

from abc                        import ABC, abstractmethod
from fastapi                    import HTTPException
import pandas as pd

from app.handler.model_connector        import ModelConnector
from app.models.inputs.text             import TextInput
from app.utils                          import log_config


log = log_config.getLogger(__name__)

class AbstractHandler(ABC):
    """
    Abstract handler class

    """
    @abstractmethod
    def handle(self):
        pass


class SimpleHandler(AbstractHandler):
    """
        Simple Handler class for demonstration
    """
    def __init__(
            self,
            ModelConnector = ModelConnector, 
            model_name: str = 'model_name',
            model_version: str = 'model_version'
        ):
        """
            Constructor of the SimpleHandler class
        """
        super(SimpleHandler, self).__init__()

        # Initialization
        self.content = None
        self.predictor = ModelConnector().get_predictor(model_name, model_version)

    def handle(self, textInput: TextInput):
        """
            Core method of the handler class.
            Handle the given textInput.
        """
        log.info('Handling the request')
        print(type(textInput))
        df = pd.DataFrame({'text': [textInput.text]})
        result = self.predictor.predict(df)

        return result[0].item()
