from django.urls import path
from app3 import views

urlpatterns=[
	path('d/',views.demo),
	path('reg/',views.reg),
]