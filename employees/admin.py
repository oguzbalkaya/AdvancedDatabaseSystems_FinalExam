from django.contrib import admin
from .models import EmployeeInfo,Field
@admin.register(EmployeeInfo)
class EmployeeInfo(admin.ModelAdmin):

    class Meta:
        model=EmployeeInfo


@admin.register(Field)
class Field(admin.ModelAdmin):

    class Meta:
        model=Field