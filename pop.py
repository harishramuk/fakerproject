import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','indiajobsproject.settings')
import django
django.setup()

from JobsApp.models import *
from faker import Faker
from random import *
fake=Faker()
def phonenumbergen():
    d1=randint(7,9)
    num=''+str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)
def populate(n):
    for i in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        ftitle=fake.random_element(elements=('Project Manager', 'TeamLead', 'Software Engineer'))
        feligibility=fake.random_element(elements=('B.Tech', 'M.Tech', 'MCA','Phd'))
        faddress=fake.address()
        femail=fake.email()
        fphonenumber=phonenumbergen()
        Chennaijob_record=Chennaijob.objects.get_or_create(Date=fdate,Company=fcompany,Tittle=ftitle,Eligibility=feligibility,Address=faddress,Email=femail,PhoneNO=fphonenumber)
        Banglorejob_record=Banglorejob.objects.get_or_create(Date=fdate,Company=fcompany,Tittle=ftitle,Eligibility=feligibility,Address=faddress,Email=femail,PhoneNO=fphonenumber)
        Hydjob_record=Hydjob.objects.get_or_create(Date=fdate,Company=fcompany,Tittle=ftitle,Eligibility=feligibility,Address=faddress,Email=femail,PhoneNO=fphonenumber)
        Punejob_record=Punejob.objects.get_or_create(Date=fdate,Company=fcompany,Tittle=ftitle,Eligibility=feligibility,Address=faddress,Email=femail,PhoneNO=fphonenumber)
populate(25)
