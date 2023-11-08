import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv("flipkartt2.csv")

X = df[['Original_price']]
y = df['Discounted_price']

X_train,X_test,y_train,y_test = train_test_split(X,y, test_size=0.2,random_state=42)

model=RandomForestRegressor()

model.fit(X_train,y_train)

y_pred = model.predict(X_test)

joblib.dump(model,'model.sav')