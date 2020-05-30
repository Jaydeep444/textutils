
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', include('myapp.urls')),
    path('admin', admin.site.urls),
    # path('home', views.home, name='home'),
    # path('contact', views.contact, name='contact'),
    # path('abot', views.about, name='about'),
    # path('hospital_list', views.hospital_lis, name='hospital-list'),
    # path('hospital_detail', views.hospital_detail, name='hospital-detail'),
    # path('doctor_list', views.doctor_lis, name='doctor-list'),
    # path('doctor_detail', views.doctor_detail, name='doctor-detail'),


    # path('add_hospital', views.add_hospital, name='add-hospital'),
    # path('add_doctor', views.add_doctor, name='add-doctor'),

#     path('', include('myapp.urls')),
#     path('cal', include('calc.urls')),
#     path('', admin.site.urls),
#     path('index', views.index, name='index'),
#     path('abot', views.about, name='about'),
]
