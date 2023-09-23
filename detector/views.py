# detector/views.py
from django.shortcuts import render, redirect
from .models import PhishingURL

def home(request):
    return render(request, 'home.html')

def detection(request):
    if request.method == 'POST':
        url = request.POST['url']
        # Perform phishing detection here and store the result in the database
        # For example, you can use your existing phishing detection code here
        # Set is_phishing to True or False based on the detection result
        PhishingURL.objects.create(url=url, is_phishing=True)  # Modify as needed
        return redirect('result')
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
