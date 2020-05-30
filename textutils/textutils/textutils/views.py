# def Index(request):
#     context = {
#     # 'name' : "Ram",
#     'user_list' : ['Ram','Shyam', 'Gita', 'Sita'],
#     'name': input(' Enter your Name : ')
#     }
#     return render(request, "index.html",context)

from django.http import HttpResponse
from django.shortcuts import render

def admin(request):
    return HttpResponse()

def home(request):
    return render(request, "home.html")

def contact(request):
    return render(request, "contact.html")

def about(request):
    context = {
        'stud_list': ['1. Jaydeep','2. James','3. Mark','4. Harry','5. Potter','6. Steven','7. Robert',]
    }
    return render(request, "about.html", context)

def hospital_lis(request):
    context = {
        'hosp_list' : ['1. Radiant Hospital ','2. Murke Hospital','3. Kabra Hospital','4. City Hospital','5. Kamna Hospital']
    }
    return render(request, "hospital_list.html", context)

def hospital_detail(request):
    return render(request, "hospital_detail.html")

def doctor_lis(request):
    context = {
        'doct_list': ['1. Dr. Jaydeep Gedam', '2. Dr. James Martin', '3. Dr. Mark Andry', '4. Dr. Harry Potter ',
                      '5. Dr. Peter Hardy', '6. Dr. Steven Downey' ]
    }
    return render(request, "doctor_list.html", context)

def doctor_detail(request):
    return render(request, "doctor_detail.html")

# def add_hospital(request):
#     return HttpResponse("This is Add-Hospital Page..")
#
# def add_doctor(request):
#     return HttpResponse("This is Add-Doctor Page..")









# def index(request):
#     return HttpResponse("hello jd")
#
# def about(request):
#     return HttpResponse("About jd")