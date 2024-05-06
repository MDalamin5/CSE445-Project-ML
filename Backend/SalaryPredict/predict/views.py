from django.shortcuts import render, redirect
from .forms import JobPredictionForm

# Create your views here.

"""def predict(request):
    if request.method == 'POST':
        # Print the POST data
        print(request.POST)
        
        # Retrieve specific form fields
        job_title = request.POST.get('jobTitle')
        years_experience = request.POST.get('yearsExperience')
        education_level = request.POST.get('educationLevel')
        industry = request.POST.get('industry')
        
        # Print individual form field values
        print('Job Title:', job_title)
        print('Years of Experience:', years_experience)
        print('Education Level:', education_level)
        print('Industry:', industry)
        
    return render(request, 'gs.html')"""
    
    # views.py
from django.http import JsonResponse

from django.http import JsonResponse
from django.shortcuts import render

def predict(request):
    if request.method == 'POST':
        print(request.POST)
        # Perform prediction here
        prediction_result = 96  # For simplicity
        return JsonResponse({'predicted_salary': prediction_result})
    return render(request, 'gs.html')



