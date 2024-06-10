"""
    
"""


from fastapi                          import APIRouter, HTTPException

from handler.handler                    import SimpleHandler
from utils                              import log_config
from models.inputs.text                 import TextInput

router = APIRouter(
    prefix="/predict",
)

handler = SimpleHandler(model_name='sk-learn-multinomialnb-model', model_version='2')
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

