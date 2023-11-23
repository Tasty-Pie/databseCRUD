from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Caregiver)
admin.site.register(Member)
admin.site.register(Address)
admin.site.register(Job)
admin.site.register(JobApplication)
admin.site.register(Appointment)
