from django.shortcuts import render
from .models import Salary, Vacancy, Profession

def demand_page(request):
    salaries = Salary.objects.all()
    vacancies = Vacancy.objects.all()
    professions = Profession.objects.all()
    context = {
        'salaries': salaries,
        'vacancies': vacancies,
        'professions': professions
    }
    return render(request, 'demand/demand.html', context)
