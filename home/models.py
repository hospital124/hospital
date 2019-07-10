from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
# from django.core.mail import send_mail
# from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
# from django.utils.translation import ugettext_lazy as _

# from .managers import UserManager


# class User(AbstractBaseUser, PermissionsMixin):
#     first_name = models.CharField(_('name'), max_length=30, blank=True)
#     password = models.CharField(_('password'), max_length=30, blank=True)
#     age = models.DateTimeField(_('date joined'), auto_now_add=True)
#     email = models.EmailField(_('email address'), unique=True)
#     is_active = models.BooleanField(_('active'), default=True)
   
# Create your models here.

class doctor(models.Model):
    doctor_name=models.CharField('doctor name',max_length=30,null=True)
    sex=(('male','male'),('female','female'),('others','others'))
    Sex=models.CharField('sex',choices=sex,blank=True,null=True,max_length=10)
    Contact=PhoneNumberField('Contact',null=True)
    Email=models.EmailField('Email',blank=False,unique=True,null=True)
    s=(('physician','physician'),('orthopedic','orthopedic'),('cardiologist','cardiologist'),('pediatrician','pediatrician'))
    Spec=models.CharField('specification',choices=s,blank=True,null=True,max_length=15)
    av=models.BooleanField('Avaialable',default=True)
    pa=models.CharField('Password',blank=True,null=True,max_length=10)
    def __str__(self):
        return self.doctor_name

class patient(models.Model):
    patient_name=models.CharField('Patient name',max_length=30,null=True)
    sex=(('male','male'),('female','female'),('others','others'))
    Sex=models.CharField('sex',choices=sex,blank=True,null=True,max_length=10)
    Dob=models.DateField('Date of Birth',null=True,blank=True)
    Age=models.IntegerField()
    #password=models.PasswordField()
    Contact=PhoneNumberField('Contact',null=True)
    Address=models.CharField('Address',max_length=200,null=True)
    Email=models.EmailField('Email',blank=False,unique=True,null=True)
    blood_group=(('ab+','AB+'),('ab-','AB-'),('a+','A+'),('a-','A-'),('b+','B+'),('b-','B-'),('o-','O-'),('o+','O+'))
    Blood_group=models.CharField('blood group',max_length=4,choices=blood_group,blank=True)
    s=(('physician','physician'),('orthopedic','orthopedic'),('cardiologist','cardiologist'),('pediatrician','pediatrician'))
    spec=models.CharField('specification',choices=s,blank=True,null=True,max_length=15)
    pa=models.CharField('Password',blank=True,null=True,max_length=10)
    
    def __str__(self):
        return self.patient_name

