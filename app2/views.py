from django.shortcuts import render

# Create your views here.

def india(request):
    return render(request,'india.html')

def australia(request):
    return render(request,'australia.html')

def SA(request):
    return render(request,'SA.html')