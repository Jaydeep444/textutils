from django.contrib import admin

from .models import Employee
admin.site.register(Employee)

from .models import hospital_detail
admin.site.register(hospital_detail)

from .models import doctor_detail
admin.site.register(doctor_detail)

from .models import patient_detail
admin.site.register(patient_detail)

from .models import contact_us
admin.site.register(contact_us)








# from .models import hospital_detail
# admin.site.register(hospital_detail)
#
# from .models import doctor_detail
# admin.site.register(doctor_detail)
#
# from .models import patient_detail
# admin.site.register(patient_detail)
#
# from .models import contact_us
# admin.site.register(contact_us)