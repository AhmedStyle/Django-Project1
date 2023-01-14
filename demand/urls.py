from django.urls import path
from .views import demand_page

urlpatterns = [
    path('demand.html', demand_page, name='demand.html'),
]
