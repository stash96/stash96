import uvicorn
from typing import Dict, Optional
from fastapi import FastAPI
# from LOT_AD_production.inference import load_pickle
# from LOT_AD_production.inference import get_output

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello":"World?!"}

# @app.get("/load")
# def load():
#     global model
#     model = load_pickle("/model/latest.pkl")
#     return {"모델":model}

# @app.get("/classification")
# def classification(q: Optional[str] = None):
#     output = get_output(model, {"측정명A1":0.0592}, ["측정명1", "측정명2", "측정명3"])
#     return output