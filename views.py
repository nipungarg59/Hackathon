from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import HttpResponseRedirect, HttpResponse
import csv
import subprocess,datetime
from subprocess import PIPE
import time
from random import randint,shuffle


@csrf_exempt
def getReport(request):
	try:
		if(request.FILES):
			print (request.FILES)
		data = {}
		data['radius_mean'] = request.POST.get('radius_mean')
		data['area_mean'] = request.POST.get('area_mean')
		data['concave_points_mean'] = request.POST.get('concave_points_mean')
		data['concavity_mean'] = request.POST.get('concavity_mean')
		data['perimeter_mean'] = request.POST.get('perimeter_mean')
		f = csv.writer(open("test.csv", "wb+"))
		f.writerow(["radius_mean", "area_mean", "concave points_mean", "concavity_mean", "perimeter_mean"])
		f.writerow([data['radius_mean'],data['area_mean'],data['concave_points_mean'],data['concavity_mean'],data['perimeter_mean']])
		# print (request.FILES)
		response = "default"
		response1 = subprocess.Popen(["python","predict.py"], stdout=PIPE, stderr=PIPE)
		(response,error) = response1.communicate()
		while(response=="default"):
				pass
		return JsonResponse({'error': False,'response':response})
	except:
		return JsonResponse({'error': True})