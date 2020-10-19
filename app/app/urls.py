"""app URL Configuration

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
from django.urls import path

from customer.views import register, loginPage, logoutUser, index, \
    create_customer, update_customer, delete_customer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('login/', loginPage, name="login"),
    path('register/', register, name="register"),
    path('logout/', logoutUser, name="logout"),
    path('create_customer/', create_customer, name="create_customer"),
    path('update_customer/<str:pk>/', update_customer, name="update_customer"),
    path('delete_customer/<str:pk>/', delete_customer, name="delete_customer"),
]
