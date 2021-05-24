from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='mainsite_index'),
    path('calculator/',views.calculator,name='mainsite_calculator'),
]