"""project_healthcae URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.views.generic import TemplateView

from app_healthcare import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.showindex.as_view(),name='index'),
    path('user_registration/',views.UserRegistration.as_view(),name='user_registration'),
    path('admin_log/',TemplateView.as_view(template_name="adminlog.html"),name='admin_log'),
    path('admin_home/',views.AdminHome.as_view(),name='admin_home'),
    path('disease/',views.disease_form,name='disease'),
    path('disease_data/',views.disease_data,name='disease_data'),
    path('all_diseases/',views.all_disease_data,name='all_diseases'),
    path('all_medicines/',views.all_medicine_data,name='all_medicines'),
    path('update_disease/',views.update_disease,name='update_disease'),
    path('update_disease_data/',views.update_disease_data,name='update_disease_data'),
    path('delete_disease/',views.delete_disease,name='delete_disease'),
    path('medicine/',views.medicine_form,name='medicine'),
    path('medicine_data/',views.medicine_data_save,name='medicine_data'),
    path('update_medicine/',views.medicine_update,name='update_medicine'),
    path('update_medicine_data/',views.medicine_update_data,name='update_medicine_data'),
    path('delete_medicine/',views.delete_medicine,name='delete_medicine'),
    path('all_register_users/',views.all_register_users,name='all_register_users'),
    path('all_medicines_diseases/',views.all_medicine_diseases,name='all_medicines_diseases'),

    #user
    path('user_login/',views.user_login,name='user_login'),
    path('userhome_login/',views.userhome_page_login,name='userhome_login'),
    path('user_report/',views.user_report,name='user_report'),
    path('search_medicine/',views.search_medicine,name='search_medicine'),
    path('search_medicine_data/',views.search_medicine_data,name='search_medicine_data'),
    path('change_password/',views.change_password,name='change_password'),
    path('password_data/',views.change_password_data,name='password_data'),
]
