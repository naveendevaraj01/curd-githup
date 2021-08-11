from django.shortcuts import render, redirect
from data.forms import EmployeeForm
from data.models import Employee
from django.http import HttpResponse


def index(request):
    obj = Employee.objects.all()
    return render(request, 'index.html',{'data':obj})

def create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('read')
        return redirect('create')
    else:
        form=EmployeeForm
    context = {
        "form":form
    }
    return render(request, 'create.html',context)

def update(request, id):
    obj = Employee.objects.get(id=id)
    if request.method == 'POST':
        form=EmployeeForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('read')
        return redirect('update')
    else: 
        form = EmployeeForm
    return render(request, 'update.html',{"emp":form})

def delete(request,id): 
        emp = Employee.objects.get(id=id)
        emp.delete()
        return redirect('read')
