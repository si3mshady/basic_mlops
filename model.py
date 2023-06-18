import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
import numpy as np
import pickle
# the "Decision Tree Regressor" tool is like a flowchart with questions. 
# It asks questions about the features of the apple, 
# like "Is the apple red?" or "Is the apple larger than a tennis ball?" 
# Based on the answers to these questions, it follows different paths in the flowchart until it reaches a final prediction. 
# For example, if the apple is red and smaller than a tennis ball, it might predict a weight of 150 grams.

data = pd.read_csv('retail_price.csv')
# print(data.head())
data['comp_price_diff'] = data['unit_price'] - data['comp_1'] 

avg_price_diff_by_category = data.groupby('product_category_name')['comp_price_diff'].mean().reset_index()

X = data[['qty', 'unit_price', 'comp_1', 'product_score', 'comp_price_diff']].astype(float) #features
y = data['total_price'].astype(float) #features

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=42)

model = DecisionTreeRegressor()

model.fit(X, y)#train model on data
# y_prediction = model.predict(X) #y= price prediction
#  qty  unit_price  comp_1  product_score  comp_price_diff  = features 
test_values = np.array([[4,88,19,4,33]]).astype(float)

price_result = model.predict(test_values)
print(price_result)


data = {"model": model}

with open('price_prediction_model.pkl', 'wb') as file:
    pickle.dump(data,file)


