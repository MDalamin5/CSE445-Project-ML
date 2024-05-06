from django.db import models

# Create your models here.

class JobPrediction(models.Model):
    job_title = models.CharField(max_length=100)
    years_experience = models.CharField(max_length=100)
    education_level = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
