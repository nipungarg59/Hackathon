import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import KFold   #For K-fold cross validation
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn import metrics


df = pd.read_csv("data.csv")
test = pd.read_csv("test.csv")
df.drop('id',axis=1,inplace=True)
df.drop('Unnamed: 32',axis=1,inplace=True)

df['diagnosis'] = df['diagnosis'].map({'M':1,'B':0})
f = csv.writer(open("data.csv", "a"))

def classification_model(model, data,test, predictors, outcome):
	model.fit(data[predictors],data[outcome])

	
	predictions = model.predict(test[predictors])
	print(predictions[0])
	if predictions[0] == 1:
		f.writerow([0,'M',test['radius_mean'],0,test['perimeter_mean'],test['area_mean'],0,0,0,test['concave points_mean'],0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ])
	else:
		f.writerow([0,'B',test['radius_mean'],0,test['perimeter_mean'],test['area_mean'],0,0,0,test['concave points_mean'],0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ])



predictor_var = ['radius_mean','area_mean','concave points_mean','concavity_mean','perimeter_mean']
outcome_var = 'diagnosis'
model = RandomForestClassifier(n_estimators=100,min_samples_split=25, max_depth=7, max_features=2)
classification_model(model,df,test ,predictor_var,outcome_var)