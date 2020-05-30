from django.urls import path
from . import views

urlpatterns = [
    # path('users/', views.Users_index, name="user_list"),
    # path('users/<str:name>/', views.Users_by_name, name="user_list_by_name"),
    # path('index/', views.Index, name="index"),

    # path('index/', views.Index, name="index"),
    path('', views.Myhome, name="Myhome"),
    path('employee', views.Add_employee, name="add_employee"),
    path('add_hospital', views.Add_hospital, name="add_hospital"),
    path('add_doctor', views.Add_doctor, name="add_doctor"),
    path('add_patient', views.Add_patient, name="add_patient"),
    path('contact_us', views.contact_us, name="contact_us"),

    # path('Users/', views.Users_index, name="user_list"),
    # path('Users/<str:name>/', views.Users_by_name, name="user_list_by_name"),
]