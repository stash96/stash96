from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, Optional
from enum import Enum

from LOT_AD_production.inference import load_pickle
from LOT_AD_production.inference import get_output

import uvicorn
# constants (PATHS)
from configs import MODEL_PATH

app = FastAPI()

# class mlModel(BaseModel):
#     modelName: str
#     modelDescription: Optional[str] = "Default model description."

try:
    model = load_pickle(MODEL_PATH)
except Exception as e:
    print(e)

@app.get("/")
def start_logics():
    # 구조!
    # api로 input을 받을 때, body로, BaseModel(body)
    # Class 형태로 받아들여서 사용할 것.
    global model
    
    return {"output data": model.get_params()}

@app.get("/modelparams")
def getModelParams():
    
    return {"Parameters":model.get_params()}