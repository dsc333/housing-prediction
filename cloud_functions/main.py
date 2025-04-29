# Deploy as a Cloud Function on GCP
# To run, first copy model pickle file (housing-rf.pkl)
# to Cloud Storage.  Initialize the requirements file
# on Cloud Function (in the "Source" tab) using the modules
# listed in requirements.txt included here.  
import functions_framework
from google.cloud import storage
import joblib
import json
import os

@functions_framework.http
def predict(request):
    # Initialize bucket_name based on your bucket name on GCP
    bucket_name = "YOUR BUCKET NAME"
    model_file_name = "housing-rf.pkl"
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(model_file_name)
    local_file_path = f"/tmp/{model_file_name}"

    # Download model from Cloud Storage
    blob.download_to_filename(local_file_path)

    # Load the model
    model = joblib.load(local_file_path)

    # Get request data
    request_json = request.get_json(silent=True)
    if not request_json: 
        return ("Please provide data in JSON format", 400,)

    # Extract the fields from the JSON request object
    bedrooms = request_json["bedrooms"]
    bathrooms = request_json["bathrooms"]
    living_sqft = request_json["living_sqft"]
    lot_size = request_json["lot_size"]

    # Make prediction and return result to client
    rf_prediction = model.predict([[bedrooms, bathrooms, living_sqft, lot_size]])
    estimate = {"estimate": str(rf_prediction)}
    return json.dumps(estimate), 200
