from django import forms
from .models import Employee
from .models import hospital_detail
from .models import doctor_detail
from .models import patient_detail
from .models import contact_us

class Employee_form(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

class hospital_form(forms.ModelForm):
    class Meta:
        model = hospital_detail
        fields = "__all__"

class doctor_form(forms.ModelForm):
    class Meta:
        model = doctor_detail
        fields = "__all__"

class patient_form(forms.ModelForm):
    class Meta:
        model = patient_detail
        fields = "__all__"

class contactus_form(forms.ModelForm):
    class Meta:
        model = contact_us
        fields = "__all__"