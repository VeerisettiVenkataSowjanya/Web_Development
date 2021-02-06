"""Project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sampletext/',views.sample1),
    path('greet/',views.sample2),
    path('paragraph/',views.sample3),
    path('example/',views.sample4),
    path('input/<str:name>/<int:age>/',views.sample5),
    path('samplehtml/',views.samplehtmlex,name='sampletextex'),
    path('internalcss/',views.internalcssex,name='internalcssex'),
    path('externalcss/',views.externalcssex,name='externalcssex'),
    path('bootex/',views.bootstrapex,name="bootstrapex"),
    path('login/',views.login,name="loginex"),
    path('register/',views.register,name="register"),
    path('',include('app2.urls')),
    path('forms/',include('app3.urls')),
]
