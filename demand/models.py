from django.db import models
class Salary(models.Model):
    year = models.IntegerField()
    level = models.DecimalField(max_digits=5, decimal_places=2)

class Vacancy(models.Model):
    year = models.IntegerField()
    number = models.IntegerField()

class Profession(models.Model):
    name = models.CharField(max_length=100)
    salary_level = models.DecimalField(max_digits=5, decimal_places=2)
    salary_year = models.IntegerField()
    vacancy_number = models.IntegerField()
    vacancy_year = models.IntegerField()
