# House price estimator

### VM deployment (top-level directory)
*housing-build-model.py*: Build an RF and KNN model based on King County housing dataset.  Model are saved to housing-knn.pkl and housing-rf.pkl.  Only run once to create pickle files. 

*housing-predict.py*: FastAPI app with a single endpoint that returns price estimate given: # bedrooms, # bathrooms, living space, lot size.  API uses previously trained KNN model (generated from file above).  

*housing_streamlit.py*: Streamlit client application that invokes the API based on values input by the user.  

*requirements.txt*: Python modules required to run sever applications.  Create a Python virtual environment and then: pip3 install -r requirements.txt

### GCP Cloud Function Deployment (cloud_functions subdirectory)

*main.py*: Code for cloud function to be stored on GCP.  To run, first copy the housing-rf.pkl to Cloud Storage and update bucket_name accordingly.

*requirements.txt*: Requirements file for GCP cloud function.  

*housing-streamlit-cf.py*: Updated streamlit application to work with cloud function deployment.  Initialize the URL first.  

 
