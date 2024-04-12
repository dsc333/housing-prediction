# House price estimator

*housing-build-model.py*: Build a KNN model based on King County housing dataset.  Model is saved to housing-knn.pkl.  Only run once to create pickle file. 

*housing-predict.py*: FastAPI app with a single endpoint that returns price estimate given: # bedrooms, # bathrooms, living space, lot size.  API uses previously trained KNN model (generated from file above).  

*housing_streamlit.py*: Streamlit client application that invokes the API based on values input by the user.  

*requirements.txt*: Python modules required to run sever applications.  Create a Python virtual environment and then: pip3 install -r requirements.txt
