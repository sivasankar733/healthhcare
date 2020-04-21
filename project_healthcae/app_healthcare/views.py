from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import View
from .models import UserLoginModel,DiseaseModel,MedicineModel
from .forms import UserLoginForm,DiseaseForm,MedicineForm

class showindex(View):
    def get(self,request):
        return render(request,"hompage.html")

class UserRegistration(View):
    def get(self,request):
        ulm=UserLoginModel.objects.all()
        return render(request,"userlogin.html",{"ul":UserLoginForm(),"um":ulm})
    def post(self,request):
        ulf=UserLoginForm(request.POST)
        if ulf.is_valid():
            ulf.save()
            messages.success(
                request,"user details was saved")
            return redirect('user_registration')
        else:
            ulm=UserLoginModel()
            return render(request,"userlogin.html",{"uf":ulf,"um":ulm})

class AdminHome(View):
    def post(self,request):
        una=request.POST.get("uname")
        pa=request.POST.get("pas")
        if una=="admin" and pa=="admin":
            return render(request,"adminhome.html")
        else:
            messages.success(request,"username and password invaid")
            return render(request,"adminlog.html")

    def get(self,request):
        return render(request,"adminhome.html")


def disease_form(request):
    return render(request,"disease.html",{"df":DiseaseForm(),"dm":DiseaseModel()})

def disease_data(request):
    df=DiseaseForm(request.POST)
    if df.is_valid():
        df.save()
        return redirect("all_diseases")
    else:
        return render(request,"disease.html",{"df":df})

def all_disease_data(request):
    return render(request,"all_diseases.html",{"dm":DiseaseModel.objects.all()})

def update_disease(request):
    dname=request.GET.get("dname")
    dsym=request.GET.get("dsym")
    d1={"dname":dname,"dsym":dsym}
    return render(request,"disease.html",{"dupdate_data":d1,"dm":DiseaseModel.objects.all()})

def update_disease_data(request):
    dname=request.POST.get('t1')
    dsym=request.POST.get('t2')
    DiseaseModel.objects.filter(des_name=dname).update(des_sym=dsym,des_name=dname)
    return redirect('all_diseases')

def delete_disease(request):
    dname=request.GET.get('dname')
    DiseaseModel.objects.filter(des_name=dname).delete()
    return redirect('all_diseases')

def medicine_form(request):
    return render(request,"medicine.html",{"mf":MedicineForm(),"dm":MedicineModel.objects.all()})


def medicine_data_save(request):
    mf=MedicineForm(request.POST)
    if mf.is_valid():
        mf.save()
        return redirect('all_medicines')
    else:
        return render(request,"medicine.html",{"mf":mf})


def all_medicine_data(request):
    return render(request,"all_medicines.html",{"dm":MedicineModel.objects.all()})

def medicine_update(request):
    mno=request.GET.get("mno")
    mname=request.GET.get("mname")
    mdesc=request.GET.get("mdesc")
    d1={"mno":mno,"mname":mname,"mdesc":mdesc}
    return render(request,"medicine.html",{"dupdate_data":d1,"dm":MedicineModel.objects.all()})


def medicine_update_data(request):
    mno=request.POST.get("t1")
    mname=request.POST.get("t2")
    mdesc=request.POST.get("t3")
    MedicineModel.objects.filter(medcine_no=mno).update(medcine_description=mdesc,medcine_name=mname)
    return redirect('all_medicines')

def delete_medicine(request):
    mname=request.GET.get("mname")
    MedicineModel.objects.filter(medcine_name=mname).delete()
    return redirect('all_medicines')

def all_register_users(request):
    return render(request,"all_registers.html",{"rmdata":UserLoginModel.objects.all()})

def all_medicine_diseases(request):
    return render(request,"all_medicines_disases.html",{"dm":MedicineModel.objects.all()})

def user_login(request):
    return render(request,"user_page_login.html")


def userhome_page_login(request):
    uname=request.POST.get("username")
    pas=request.POST.get("password")
    try:
        UserLoginModel.objects.get(usermname=uname,password=pas)
        return render(request,"user_homepage_login.html")
    except UserLoginModel.DoesNotExist:
        messages.success(request,"invalid usernam and password")
        return redirect("user_login")


def user_report(request):
    return render(request,"user_report.html")

def search_medicine(request):
    return render(request,"searhmedicine.html")


def search_medicine_data(request):
    dname=request.POST.get("dname")
    try:
        MedicineModel.objects.get(disease__des_name=dname)
        return render(request,"showmedicine_details.html",{"dm":MedicineModel.objects.all()})
    except MedicineModel.DoesNotExist:
        return redirect('search_medicine')


def change_password(request):
    return render(request,"change_password.html",{"uf":UserLoginForm(),"um":UserLoginModel.objects.all()})


def change_password_data(request):
    opas=request.POST.get("oldpas")
    npas=request.POST.get("newpas")
    try:
        UserLoginModel.objects.get(password=opas)
        UserLoginModel.objects.filter(password=opas).update(password=npas)
        messages.success(request, "password was changed")
        return redirect('change_password')
    except UserLoginModel.DoesNotExist:
        messages.success(request,"invalid password")
        return redirect('change_password')