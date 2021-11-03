import uvicorn
from typing import Dict, Optional
from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum
import pickle
from LOT_AD_production.inference import load_pickle
from LOT_AD_production.inference import get_output

app = FastAPI()

# # FAST API practice
# # ------------------------------------------------------------------------------

# class ModelName(str, Enum):
#     alexnet = "alexnet"
#     resnet = "resnet"
#     lenet = "lenet"

# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None

# fake_items_db = [
#     {"item_name": "Foo"},
#     {"item_name": "Bar"},
#     {"item_name": "Baz"}
# ]

# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip : skip + limit]
# # ------------------------------------------------------------------------------
# # [GET]
# # @app.get("/items/{item_id}")
# # async def read_item(item_id: str, q: Optional[str] = None, short: bool = False):
# #     # bool --> 1, True, true, on, yes 다 같은 것.
# #     item = {"item_id": item_id}
# #     if q:
# #         return {"item_id": item_id, "q": q}
# #     if not short:
# #         item.update(
# #             {"description": "This is an amazing item that has a long description"}
# #         )
# #     return item

# @app.get("/users/{user_id}/items/{item_id}")
# async def read_user_item(user_id: int, item_id: str, q: Optional[str] = None, short: bool = False):
#     item = {"item_id": item_id, "owner_id": user_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item

# @app.get("/items/{item_id}")
# async def read_user_item(item_id: str, needy: str):
#     item = {"item_id": item_id, "needy": needy}
#     return item

# @app.get("/items/{item_id}")
# async def read_user_item(item_id: str, needy: str, skip: int = 0, limit: Optional[int] = None):
#     item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
#     return item

# @app.get("/")
# def read_root():
#     return {"message":"Hello there?"}


# @app.post("/items")
# async def create_item(item: Item):
#     return item

# @app.get("/users/me")
# async def read_user_me():
#     return {"user_id": "the current user"}

# @app.get("/users/{user_id}")
# async def read_user(user_id: str):
#     return {"user_id": user_id}

# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name == ModelName.alexnet:
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}
#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": "LeCNN all the images"}
    
#     return {"model_name": model_name, "message": "Have some residuals"}

# @app.get("/files/{file_path:path}")
# async def read_file(file_path: str):
#     return {"file_path": file_path}
# # [GET]
# # ------------------------------------------------------------------------------
# # [POST]
# @app.post("/items/")
# async def create_item(item: Item):
#     return item

# # ------------------------------------------------------------------------------
# @app.get("/load")
# def load():
#     global model
#     model = load_pickle("/model/latest.pkl")
#     return {"모델":model}

# @app.get("/classification")
# def classification(q: Optional[str] = None):
#     output = get_output(model, {"측정명A1":0.0592}, ["측정명1", "측정명2", "측정명3"])
#     return output


# ------------------------------------------------------------------------------
@app.get("/")
def start_logics():
    with open('/model/model1.pkl', 'rb') as f:
        model = pickle.load(f)
        #DecisionTreeClassifier Model
    # model = load_pickle("./model1.pkl")
    # print(model)
    # sample = (model, {"부품명예시1번": 0.17527}, ["측정명"])
    # output = get_output(sample)
    # print(output)
    return {"data":model.get_params()}

# global model
# model = myLoad("/model/model1.pkl")
# ------------------------------------------------------------------------------