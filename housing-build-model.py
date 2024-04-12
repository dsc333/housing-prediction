# DSC 333
# Builds KNN regression model from the kc_house_data dataset
# and pickles it to current directory

# Only run once to generate the .pkl file.  Must be executed
# in the same folder as the FastAPI server app. 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
import pickle

print('Building KNN model. This may take a while.')

df = pd.read_csv('https://raw.githubusercontent.com/dsc333/housing-prediction/main/kc_house_data.csv')


# Define the X columns (independent variables / features).  We're selecting
# a small subset of the features available in the dataset.
# Define y variable (output variable - what we want to predict)

X = df.loc[:, ['bedrooms','bathrooms', 'sqft_living', 'sqft_lot']]
y = df.loc[:, 'price']

# Generate the train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=1)

# define the model.  Neighborhood size = 15 (try changing the neighborhood size)
knn = KNeighborsRegressor(n_neighbors = 15, weights = 'uniform')

# "Train" the model
knn.fit(X_train, y_train)

# Run the model to make predictions based on test data
y_pred = knn.predict(X_test)

print('R squared: ', knn.score(X_test, y_test))

# Save model to pickle file for use by API 
pickle.dump(knn, open('housing-knn.pkl', 'wb'))
