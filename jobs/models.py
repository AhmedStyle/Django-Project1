from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    skills = models.TextField()
    company = models.CharField(max_length=255)
    salary = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    posted_date = models.DateField()
