# DSC 333: Streamlit app for housing price predictor API
# Uses a model deployed as Cloud Function on GCP
import streamlit as st
import requests

st.title('House price estimator')

with st.form(key='my_form'):
    bedrooms = st.slider('Bedrooms', 0, 20, 3)
    bathrooms = st.slider('Bathrooms', 0, 10, 2)
    living_sqft = st.slider('Living space (sq. ft.)', 800, 5000, 1500)
    lot_size = st.slider('Lot size (sq. ft.)', 2000, 50000, 10000)
    submitted = st.form_submit_button(label='Estimate price')

    if submitted:
    
        # Replace URL using your GCP cloud function URL and append the 
        # function entry point to it
        # EXAMPLE: URL = 'https://dsc333-876203476.us-central1.run.app/predict'
        URL = "Your cloud function url and function"
        
        params = {'bedrooms':int(bedrooms),
                  'bathrooms':int(bathrooms),
                  'living_sqft':int(living_sqft),
                  'lot_size':int(lot_size)}
        
        # Cloud function uses a POST request
        r = requests.post(URL, json=params)
        if r:
            r_json = r.json()
            print(r_json['estimate'])
            st.subheader('Estimated price:')

            estimate = r_json['estimate']

            # remove brackets and decimal values and display result
            estimate = estimate[1:estimate.index('.')]
            st.text('$'+estimate)
        else:
            st.text('Price could not be retrieved.')
