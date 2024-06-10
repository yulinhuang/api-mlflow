"""
    A Python API interface implementation for MLflow Model serving using FastAPI.

    main file for launching the API interface
    
"""

import os

from fastapi            import Depends, FastAPI
from fastapi.responses  import HTMLResponse

from app.routers        import predict







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