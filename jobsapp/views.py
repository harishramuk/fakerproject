from django.shortcuts import render
from JobsApp.models import *

# Create your views here.
def index(request):
    return render (request,'jobsapp/index.html')
def chennai(request):
    jobs_list = Chennaijob.objects.order_by('Date')
    my_dir = {'jobs_list':jobs_list}
    return render(request,'jobsapp/chennai.html',context = my_dir)
def banglore(request):
    jobs_list = Banglorejob.objects.order_by('Date')
    my_dir = {'jobs_list':jobs_list}
    return render(request,'jobsapp/banglore.html',context = my_dir)
def hyd(request):
    jobs_list = Hydjob.objects.order_by('Date')
    my_dir = {'jobs_list':jobs_list}
    return render(request,'jobsapp/hyd.html',context = my_dir)
def pune(request):
    jobs_list = Punejob.objects.order_by('Date')
    my_dir = {'jobs_list':jobs_list}
    return render(request,'jobsapp/pune.html',context = my_dir)
