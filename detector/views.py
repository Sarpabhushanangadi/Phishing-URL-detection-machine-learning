# detector/views.py
import numpy as np
from django.shortcuts import render, redirect
from .features import FeatureExtraction
from sklearn.ensemble import GradientBoostingClassifier
from sklearn import metrics
import pickle
import pandas as pd
from django.http import HttpResponse

file = open("C:\\Django\\phishing_detector\\detector\\model.pkl", "rb")
gbc = pickle.load(file)
file.close()


def home(request):
    return render(request, 'home.html')

def detection(request):
    if request.method == 'POST':
        url = request.POST.get('url', '')
        
        obj = FeatureExtraction(url)
        x = np.array(obj.getFeaturesList()).reshape(1, 30)

        y_pred = gbc.predict(x)[0]
        y_pro_phishing = gbc.predict_proba(x)[0, 0]
        y_pro_non_phishing = gbc.predict_proba(x)[0, 1]
        y1=y_pro_phishing*100
        y2=y_pro_non_phishing*100

        response_data = {
            'url': url,
            'prediction': y_pred,
            'probability_phishing': y1,
            'probability_non_phishing': y2,
        }

        return render(request, 'result.html', response_data)

    return render(request, 'detection.html')
    

    
    

# views.py
import csv
from django.shortcuts import render

def dataset(request):
    # Path to your CSV file
    csv_file_path = 'C:\\Django\\phishing_detector\\dataset_phishing.csv'

    # Read the CSV file
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)

    # Pass the data to the template
    return render(request, 'dataset.html', {'data': data})



def result(request):
    
    return render(request, 'result.html')
