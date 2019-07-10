from django.shortcuts import render,redirect,HttpResponse
from home.models import patient,doctor
# from django.contrib.auth import logout,login
from home.forms import patientsearchform
# from . forms import UserloginForm
# Create your views here.
def home_view(request):
    return render(request,'home.html')

def doctorlogin(request):
    if request.method=='POST':
        username=request.POST.get('doctor')
        password=request.POST.get('pas')
        try:
            user=doctor.objects.get(doctor_name=username)
            if user:
                if user.pa==password:
                    temp='/doctorpage/'
                    return redirect(temp)
                else:
                    return HttpResponse('incorrect password')
        except doctor.DoesNotExist:
            user=None
            print('Someone tried to login and failed')
            print('they used username:{} password:{}'.format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request,'auth/doctorlogin.html',{})
# try:
#     user = UniversityDetails.objects.get(email=email)
# except UniversityDetails.DoesNotExist:
#     user = None
def doctorpage(request):
    if request.method=='POST':
        search=patientsearchform(request.POST)
        if search.is_valid():
            value=search.cleaned_data.get('q')
            result=patient.objects.filter(patient_name__contains=value)
            return render(request,'home1.html',{'result':result,'form':patientsearchform()})
    else:
        form=patientsearchform()
        #result=patient.objects.all()
        return render(request,'home1.html',{'form':form})

def patientlogin(request):
    if request.method=='POST':
        username=request.POST.get('patient')
        password=request.POST.get('pas')
        try:
            user=patient.objects.get(patient_name=username)
            if user:
                if user.pa==password:
                    temp='/patient/'
                    return redirect(temp)
                else:
                    return HttpResponse('incorrect password')
        except doctor.DoesNotExist:
            user=None
            print('Someone tried to login and failed')
            print('they used username:{} password:{}'.format(username,password))
            return HttpResponse("Invalid login details given")
    else:
         return render(request,'auth/patientlogin.html',{})
# def token(request):

