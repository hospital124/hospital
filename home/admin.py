from django.contrib import admin
from home.models import patient,doctor

# Register your models here.
@admin.register(patient)
class patientAdmin(admin.ModelAdmin):
    pass

@admin.register(doctor)
class doctorAdmin(admin.ModelAdmin):
    pass
