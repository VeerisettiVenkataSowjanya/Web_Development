from django.urls import path
from app2 import views

urlpatterns=[
	path('demo/',views.demo),
	path('',views.home,name='home'),
	path('addstudent/',views.addstudent,name='addstudent'),
	path('details2/',views.details2,name='details2'),
	path('update/<int:id>',views.update,name='update'),
	path('delete/<int:id>',views.delete,name='delete'),

]