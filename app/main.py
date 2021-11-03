import uvicorn
from typing import Dict, Optional
from fastapi import FastAPI
from LOT_AD_production.inference import load_pickle
from LOT_AD_production.inference import get_output

app = FastAPI()

@app.get("/load")
def load():
    global model
    model = load_pickle("/model/latest.pkl")
    return {"모델":model}

@app.get("/classification")
def classification(q: Optional[str] = None):
    output = get_output(model, {})

    return output
# def load_model(model_path: str):
#     # 경로로 모델 오브젝트 return
#     model = (model_path)
#     # model_path == "/model/latest.pkl"

#     return model

# def classification(input_tuple):
#     model_ = input_tuple[0]
    
#     device = input_tuple[1]
#     device_name = device[0]
#     cal_dict = device[1]
#     cal_name = cal_dict[0]
#     cal_value = cal_dict[1]

#     cal_name_list = input_tuple[2]
    
#     output_tuple = (str, {"causing_component_name": {"":""}})

#     return output_tuple

if __name__ == '__main__':
    uvicorn.run(app='main:app', host="127.0.0.1", port=8000, reload=True, debug=True)