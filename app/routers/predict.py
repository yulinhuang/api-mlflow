"""
    
"""


from fastapi                          import APIRouter, HTTPException

from app.handler.handler                    import SimpleHandler
from app.utils                              import log_config
from app.models.inputs.text                 import TextInput

router = APIRouter(
    prefix="/predict",
)

handler = SimpleHandler(model_name='20news-test', model_version='5')
log = log_config.getLogger(__name__)


@router.post("/")
async def predict(input_data: TextInput):
    # Convert input data to a format suitable for the model
    # input_dict = input_data.dict()
    result = handler.handle(input_data)
    # print('result here: ', result)
    # Make prediction
    try:
        # prediction = model.predict([features])
        return {"prediction": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

