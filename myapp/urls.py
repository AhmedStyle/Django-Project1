from django.urls import path
from . import views
from . import index


urlpatterns = [
    path('', views.home, name='home'),
    path('home.html', index.webhome, name='home.html'),
    path('demand.html', index.webdemand, name='demand.html'),
    path('skills.html', index.webskills, name='skills.html'),
    path('geography.html', index.webgeo,name='geography.html'),
    path('latest_jobs.html', index.weblatest_jobs, name='latest_jobs.html'),
]
