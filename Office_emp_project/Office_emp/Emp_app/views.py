from datetime import datetime

from django.db.models import Q
from django.shortcuts import render, HttpResponse, redirect
from .models import Employee,Role,Department
# Create your views here.

def index(request):
    return render(request, 'index.html')

def view_emp(request):
    obj = Employee.objects.all()
    context = {
        'obj':obj
    }
    return render(request, 'view_emp.html',context)

def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        department = request.POST.get('department')
        salary = int(request.POST.get('salary'))
        bonus = int(request.POST.get('bonus'))
        role = request.POST.get('role')
        phone = int(request.POST.get('phone'))
        new_obj = Employee(first_name = first_name, last_name=last_name,department_id=department, salary=salary,bonus=bonus, role_id=role,phone=phone,hire_date=datetime.now())
        new_obj.save()
        return render(request, 'index.html')
    elif request.method == 'GET':
        return render(request,'add_emp.html')
    else:
        return HttpResponse('Employee has not been added')

def remove_emp(request,emp_id=0):
    obj = Employee.objects.all()
    context = {
        'obj': obj
    }
    if emp_id:
        rem_emp = Employee.objects.get(id=emp_id)
        rem_emp.delete()
    return render(request,'remove.html',context)

def filter_emp(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        department = request.POST.get('department')
        role = request.POST.get('role')
        obj = Employee.objects.all()
        if name:
            obj = obj.filter(Q(first_name__icontains =name) | Q(last_name__icontains=name))
        if department:
            obj = obj.filter(department__name__icontains = department)
        if role:
            obj = obj.filter(role__name__icontains = role)

        context = {
            'obj':obj
        }
        return render(request,'view_emp.html',context)
    elif request.method == 'GET':
        return render(request,'filter.html')
    else:
        return HttpResponse('An accepton occur')





