# DSC 333
# House price prediction API

# To execute:
# uvicorn housing-predict:app --host=0.0.0.0 --port=8080 --reload 

from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
from fastapi import FastAPI
import pickle

app = FastAPI()
knn_model = pickle.load(open('housing-knn.pkl', 'rb'))

@app.get("/ia_estimate/")
async def price_estimate(bedrooms: int, bathrooms: int, living_sqft: int, lot_size:int):
    knn_pred = knn_model.predict([[bedrooms, bathrooms, living_sqft, lot_size]])
    estimate = {"ia_estimate": str(knn_pred)}
    return estimate
