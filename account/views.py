from django.shortcuts import render,redirect
from . models import account
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate,login,logout
from SellerAdmin.models import  ServiceType,Service
from .utils import *
from django.conf import settings
from user_in.views import user_index
User=get_user_model()
# Create your views here.
def indexPage(request):
    if not request.user.is_authenticated:
        ser = ServiceType.objects.all()
        data = Service.objects.all()
        return render(request, 'index.html', {'ser': ser,'data':data})

    elif request.user.is_customer==True:
        data = Service.objects.all()
        return render(request,'user/index.html',{'data':data})
    else:
        return render(request,'temp/index.html')







def contactPage(request):
    return render(request,'contact.html')

def servicePage(request):
    return render(request,'service.html')

def sellerindexPage(request):

    return render(request,'SellerAdmin/user/index.html')

def repairSPage(request):
    return render(request,'repairS.html')

def SelfCarePage(request):
    return render(request,'SelfCare.html')

def houseSPage(request):
    return render(request,'houseS.html')

def otherSPage(request):
    return render(request,'otherS.html')

def loginPage(request):
    if request.method == 'POST':
        email=(request.POST.get('email'))
        password=(request.POST.get('password'))
        print('hello')

        user = authenticate(username=email,password=password)
        if user is not None:
            login(request,user)
            if request.user.is_customer:
                print('hello')
                return redirect(user_index)
            else:
                return render(request,'temp/index.html')
    else:
        return render(request,'login.html',{'message':'Invalid email or password'})





def register_user(request):
    if request.method=='POST':
        first_name = request.POST.get('First_Name')
        last_name = request.POST.get('Last_Name')
        Email=request.POST.get('Email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        mobile = request.POST.get('mobile')

        if (pass1==pass2):
            try:
                User.objects.get(email=Email)
                return render(request,'register.html',{'message':'email id exist'})

            except:
                User.objects.create_user(username=Email,email=Email,password=pass1,mobile=mobile,is_customer=True,first_name=first_name,last_name=last_name)
                return render(request,'login.html')

        else:
            return render(request,'register.html')
    else:
        return render(request, 'register.html')

def SRegisterPage(request):
    if request.method=='POST':
        first_name = request.POST.get('First_Name')
        last_name = request.POST.get('Last_Name')
        Email = request.POST.get('Email')
        print('hello')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        mobile = request.POST.get('mobile')

        if (pass1 == pass2):
            try:
                User.objects.get(email=Email)
                return render(request, 'register.html', {'message': 'email id exist'})

            except:
                User.objects.create_user(username=Email, email=Email, password=pass1, mobile=mobile, is_service=True, first_name=first_name,last_name=last_name)
                return render(request, 'login.html')

        else:
            return render(request, 'register.html')
    else:
            return render(request, 'Sregister.html')



# def forgot(request):
#
#
#     email_subject = 'Interest shown in your property'  # subject of mail
#
#     email_from = settings.EMAIL_HOST_USER  # sender’s email address
#
#     email = 'kunalbode123@gmail.com'  # receivers’s address
#     sendmail(email_subject, 'mail_template', email,{'message':'hello'})
#     return render(request, 'mail_template.html')


def logout_page(request):
    logout(request)
    return redirect(indexPage)
