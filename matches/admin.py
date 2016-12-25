from django.contrib import admin
from django import forms
from django.db import models
from .models import Educator, Volunteer, MonthsForVisit

class EducatorAdmin(admin.ModelAdmin):
    #form = EducatorAdminForm
    formfield_overrides = {
        models.ManyToManyField: {'widget': forms.CheckboxSelectMultiple},
            }

admin.site.register(Volunteer)
admin.site.register(Educator, EducatorAdmin)
admin.site.register(MonthsForVisit)
