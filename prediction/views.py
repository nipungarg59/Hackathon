from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import HttpResponseRedirect, HttpResponse
import csv
import subprocess,datetime
from subprocess import PIPE
import time
from random import randint,shuffle
from .models import *

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import KFold   #For K-fold cross validation
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn import metrics




def classification_model(model, data,test, predictors, outcome):
	model.fit(data[predictors],data[outcome])
	predictions = model.predict(test[predictors])
	# if predictions[0] == 1:
	# 	f.writerow([0,'M',test['radius_mean'],0,test['perimeter_mean'],test['area_mean'],0,0,0,test['concave points_mean'],0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ])
	# else:
	# 	f.writerow([0,'B',test['radius_mean'],0,test['perimeter_mean'],test['area_mean'],0,0,0,test['concave points_mean'],0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ])
	return predictions[0]

def xyz(test):
	df = pd.read_csv("data.csv")
	df.drop('id',axis=1,inplace=True)
	df.drop('Unnamed: 32',axis=1,inplace=True)

	df['diagnosis'] = df['diagnosis'].map({'M':1,'B':0})
	# f = csv.writer(open("data.csv", "a"))
	predictor_var = ['radius_mean','area_mean','concave points_mean','concavity_mean','perimeter_mean']
	outcome_var = 'diagnosis'
	model = RandomForestClassifier(n_estimators=100,min_samples_split=25, max_depth=7, max_features=2)
	return classification_model(model,df,test ,predictor_var,outcome_var)

@csrf_exempt
def getReport(request):
	# print(request.body)
	try :
		if(request.FILES):
			print (request.FILES)
		data = {}
		data['radius_mean'] = int(request.POST.get('radius_mean'))
		data['area_mean'] = int(request.POST.get('area_mean'))
		data['concave points_mean'] = int(request.POST.get('concave_points_mean'))
		data['concavity_mean'] = int(request.POST.get('concavity_mean'))
		data['perimeter_mean'] = int(request.POST.get('perimeter_mean'))

		test = pd.DataFrame()
		test = test.append(data, ignore_index=True)
		print (data)
		print(test)
		response = xyz(test)
		return JsonResponse({'error': False,'response':int(response)})
	except:
		return JsonResponse({'error': True,'response':1})