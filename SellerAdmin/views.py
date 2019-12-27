from django.shortcuts import render,redirect
from . models import *


def indexPage(request):
    ser = ServiceType.objects.all()
    return render(request,'index.html', {'ser': ser})



def pendingactivityPage(request):
    data=Service.objects.filter(seller=request.user)


    return render(request,'temp/myproducts.html',{'data':data})

def AddDetailPage(request):
    ser=ServiceType.objects.all()
    subser=SubService.objects.all()

    return render(request,'temp/addproduct.html',{'subser':subser,'ser':ser})

def AddDetail(request):
    if request.method=='POST':
        title=request.POST.get("title")
        description=request.POST.get("description")
        price=request.POST.get("price")
        discount=request.POST.get("discount")
        fileinput=request.POST.get("fileinput")
        servicetype=request.POST.get('servicetype')
        subservice=request.POST.get('subservice')

        obj=ServiceType.objects.get(service_name=servicetype)
        obj1=SubService.objects.get(sub_name=subservice)

        Service.objects.create(title=title,description=description,price=price,discount=discount,type=obj,sub_category=obj1,seller=request.user)

        return redirect(pendingactivityPage)
    else:
        ser = ServiceType.objects.all()
        subser = SubService.objects.all()

        return render(request, 'temp/addproduct.html', {'subser': subser, 'ser': ser})

def tablePage(request):
     return render(request,'temp/table.html')

