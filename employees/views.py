from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import *
from .forms import NewEmployeeForm
from django.contrib.gis.geos import Point


def employees(request):
    if request.method == "GET":
        employees = EmployeeInfo.objects.all()
        context = {
            "employees": employees,
            "title": "Tüm çalışan listesi",
        }
        return render(request, "employee_list.html", context)


def employeeDetail(request, id):
    if request.method == "GET":
        employee = EmployeeInfo.objects.get(id=id)
        current_loc = [coord for coord in employee.current_location]
        home_loc = [coord for coord in employee.home_location]
        line = [[coord for coord in x] for x in employee.field.line]

        context = {
            "title": "Çalışan Bilgileri : {} {}".format(employee.employee.first_name, employee.employee.last_name),
            "employee": employee,
            "current_location": current_loc,
            "home_location": home_loc,
            "line": line,
        }
        return render(request, "employee_detail.html", context)


def newEmployee(request):
    form = NewEmployeeForm()
    if request.method == "POST":
        form = NewEmployeeForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            surname = form.cleaned_data.get("surname")
            name = form.cleaned_data.get("name")
            salary = form.cleaned_data.get("salary")
            home_location_lat = form.cleaned_data.get("home_location_lat")
            home_location_long = form.cleaned_data.get("home_location_long")
            field = form.cleaned_data.get("field")
            location = Point(home_location_lat, home_location_long)

            try:
                newUser = User(username=username, first_name=name, last_name=surname)
                newUser.set_password(password)
                newUser.save()
                newEmp = EmployeeInfo(employee=newUser, field=field, salary=salary, home_location=location,
                                      current_location=location)
                newEmp.save()
                messages.success(request, "Çalışan başarıyla eklendi.")
                return redirect("index")
            except:
                messages.warning(request, "Bu kullanıcı adına sahip bir çalışan var.")


    context = {
        "title": "Yeni Çalışan Ekle",
        "form": form
    }
    return render(request, "new_employee.html", context=context)
