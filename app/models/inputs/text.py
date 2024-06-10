from pydantic import BaseModel
from typing import List

# Define the input data schema using Pydantic BaseModel
class TextInput(BaseModel):
    """
    TextInput is a Pydantic model that defines the schema for the input data.

    Attributes:
        text (str): The input text data.
    """
    text: str
    # Add all features your model expects here

# Example usage:
# input_data = TextInput(text="Sample input text")
# print(input_data.text)

