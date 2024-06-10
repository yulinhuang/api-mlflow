"""
    A Python API interface implementation for MLflow Model serving using FastAPI.

    main file for launching the API interface
    
"""

import os

from fastapi            import Depends, FastAPI
from fastapi.responses  import HTMLResponse
from contextlib import asynccontextmanager

from routers        import predict

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Asynchronous context manager for managing the lifespan of the API.
    This context manager is used to load the ML model and other resources
    when the API starts and clean them up when the API stops.
    Args:
        app (FastAPI): The FastAPI application.
    """
    global model

    model_name: str = os.getenv("MLFLOW_MODEL_NAME")
    model_version: str = os.getenv("MLFLOW_MODEL_VERSION")
    # Load the ML model
    model = get_model(model_name, model_version)
    yield






app = FastAPI()
app.include_router(predict.router)


@app.get("/", response_class=HTMLResponse)
async def root():
    """
        Home page for the exposed API
    """
    return """
    <html>
        <head>
            <title>MLFlow serving API</title>
        </head>
        <body>
            <h1>MLFlow serving API</h1>
            
        </body>
    </html>
    """