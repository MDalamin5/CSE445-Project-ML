# forms.py
from django import forms
from .models import JobPrediction

class JobPredictionForm(forms.ModelForm):
    class Meta:
        model = JobPrediction
        fields = ['job_title', 'years_experience', 'education_level', 'industry']
