from typing import Dict, Optional
from fastapi import FastAPI
from pickle import load_pickle
app = FastAPI()

@app.get("/")
def read_root():
    return {"":""}

def load_model(model_path: str):
    # 경로로 모델 오브젝트 return
    model = load_pickle(model_path)

    return model

def classification(input_tuple):
    model_ = input_tuple[0]
    
    device = input_tuple[1]
    device_name = device[0]
    cal_dict = device[1]
    cal_name = cal_dict[0]
    cal_value = cal_dict[1]

    cal_name_list = input_tuple[2]
    

    output_tuple = (str, {"causing_component_name": {"":""}})

    return output_tuple