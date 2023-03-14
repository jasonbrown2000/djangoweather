from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('calculator.html', views.calculator, name="calculator"),
    

]                                                                                               
