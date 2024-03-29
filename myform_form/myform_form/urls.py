"""
URL configuration for myform_form project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("signup10_affichage/", views.signup10_affichage, name="signup10_affichage"),
    path("signup20_widget/", views.signup20_widget, name="signup20_widget"),
    path("signup30_data/", views.signup30_data, name="signup30_data"),
    path("signup30_data/signup30_reussi/", views.signup30_reussi, name="signup30_reussi"),
    path("signup31_data/", views.signup31_data, name="signup31_data"),
    path("signup31_affichage/", views.signup31_affichage, name="signup31_affichage"),
]
