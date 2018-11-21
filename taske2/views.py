from django.shortcuts import render
from .models import AddStudent
# Create your views here.
def showHome(request):
    return render(request,"home.html")


def showAddStudent(request):
    return render(request,"dataenteringpage.html")


def showGetData(request):
    sdata=AddStudent.objects.all()
    return render(request,"datashowingpage.html",{"data":sdata})


def addStudent(request):
    name=request.POST.get('s_name')
    age=request.POST.get('s_age')
    gender=request.POST.get('s_gender')
    add=AddStudent(name=name,age=age,gender=gender)
    add.save()
    return render(request,"dataenteringpage.html",{"status":"DATA SAVED SUCESSFULY"})