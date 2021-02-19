from django.urls import path
from . import views

urlpatterns = [

	path('', views.index, name='index'),
	path('', views.check_runs, name="check_runs")
]