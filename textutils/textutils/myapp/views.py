from django.shortcuts import render
# from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.
from .forms import Employee_form
from .forms import hospital_form
from .forms import doctor_form
from .forms import patient_form
from .forms import contactus_form

def Myhome(request):
    return render(request,"myhome.html")

def Add_employee(request):
    form = Employee_form()
    if request.method == "POST":
        form = Employee_form(request.POST)
        if form.is_valid():
            form.save()
            form = Employee_form()
            messages.success(request, 'Form submission successful')
            return HttpResponse('''<center><br><br><a href="http://127.0.0.1:8000/employee">Go Back</a><br><br><br><br><br><br><h1 style="color:red; background-color:powderblue;" >
                        <marquee behavior="scroll" direction="left" scrollamount="20">Information Recorded Successfully.....</marquee></h1></center>''')
        else:
            return render(request, "add_employee.html", {'form': form})
    else:
        form = Employee_form()
        return render(request, "add_employee.html", {'form': form})

def Add_hospital(request):
    form = hospital_form()
    if request.method == "POST":
        form = hospital_form(request.POST)
        if form.is_valid():
            form.save()
            form = hospital_form()
            messages.success(request, 'Form submission successful')
            return HttpResponse('''<center><br><br><a href="http://127.0.0.1:8000/add_hospital">Go Back</a><br><br><br><br><br><br><h1 style="color:red; background-color:powderblue;" >
                        <marquee behavior="scroll" direction="left" scrollamount="20">Information Recorded Successfully.....</marquee></h1></center>''')
        else:
            return render(request, "add_hospital.html", {'form': form})
    else:
        form = hospital_form()
        return render(request, "add_hospital.html", {'form': form})

def Add_doctor(request):
    form = doctor_form()
    if request.method == "POST":
        form = doctor_form(request.POST)
        if form.is_valid():
            form.save()
            form = doctor_form()
            messages.success(request, 'Form submission successful')
            return HttpResponse('''<center><br><br><a href="http://127.0.0.1:8000/add_doctor">Go Back</a><br><br><br><br><br><br><h1 style="color:red; background-color:powderblue;" >
                        <marquee behavior="scroll" direction="left" scrollamount="20">Information Recorded Successfully.....</marquee></h1></center>''')
        else:
            return render(request, "add_doctor.html", {'form': form})
    else:
        form = doctor_form()
        return render(request, "add_doctor.html", {'form': form})

def Add_patient(request):
    form = patient_form()
    if request.method == "POST":
        form = patient_form(request.POST)
        if form.is_valid():
            form.save()
            form = patient_form()
            messages.success(request, 'Form submission successful')
            return HttpResponse('''<center><br><br><a href="http://127.0.0.1:8000/add_patient">Go Back</a><br><br><br><br><br><br><h1 style="color:red; background-color:powderblue;" >
                        <marquee behavior="scroll" direction="left" scrollamount="20">Information Recorded Successfully.....</marquee></h1></center>''')
        else:
            return render(request, "add_patient.html", {'form': form})
    else:
        form = patient_form()
        return render(request, "add_patient.html", {'form': form})

def contact_us(request):
    form = contactus_form()
    if request.method == "POST":
        form = contactus_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submission successful')
            form = contactus_form()
            return HttpResponse('''<center><br><br><a href="http://127.0.0.1:8000/contact_us">Go Back</a><br><br><br><br><br><br><h1 style="color:red; background-color:powderblue;" >
            <marquee behavior="scroll" direction="left" scrollamount="20">Information Recorded Successfully.....</marquee></h1></center>''')
        else:
            return render(request, "contact_us.html", {'form': form})
    else:
        form = contactus_form()
        return render(request, "contact_us.html", {'form': form})













    # return render_to_response('contact_us', message='Information Recorded')
    # context = { 'form':form }
    # return render(request, "contact_us.html",context)

# from django.http import HttpResponse                  # import class HttpResponse
#
# def Users_index(request):                             # create a function user_index to call from urls.py file
#     user_list = ['1.ram<br>','2.shyam<br>', '3.gita<br>', '4.sita<br>']       # create a user list to pass in response
#     return HttpResponse(user_list)                    # return response with user
#
#
# def Users_by_name(request, name = None):              # pass extra parameter "name" with request parameter
#     return HttpResponse("username is " + name)        # Return name in response