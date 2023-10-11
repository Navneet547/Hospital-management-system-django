from django.shortcuts import render,redirect,HttpResponse
from django.views import View
from app.models import *
# Create your views here.


class landing(View):
    def get(self,request):
        return render(request,"landing_page.html")

        


# -----==============  Admin login ======------------------------
class admin_hos(View):
    def get(self,request):
        return render(request,"admin_page.html")
    def post(self,request):
        loc_id=request.POST.get("admin_id")
        loc_pass=request.POST.get("admin_password")
        if(1234== int(loc_id) and 1234==int(loc_pass)):
            return render(request,"homepage.html")
        else:
            data="* you entered wrong id or password"
            return render(request, "admin_page.html", {"data": data})

class userformview(View):
    def get(self,request):
        return render(request,"user_page.html")
    
class Homepageview(View):
    def get(self,request):
        return render(request,"homepage.html")
    
class doctor_detail(View):
    def get(self,request):
        data=doctor_model.objects.all()
        context={"data":data}
        return render(request,"doctor_detail.html",context)
    def post(self,request):
        name=request.POST.get('name_form')
        edu=request.POST.get('education_form')
        num=request.POST.get('number_form')
        spec=request.POST.get('specialization_form')
        exp=request.POST.get('experience_form')
        doctor_model(doc_name=name,doc_education=edu, doc_phone_number=num,doc_specialization=spec,doc_experience=exp).save()
        return redirect("/doctor_page/")


class patient_page(View):
    def get(sefl,request):
        data=patient_model.objects.all()
        context={"data":data}
        return render(request,"patient_page.html",context)
    def post(self,request):
        name=request.POST.get('pname_form')
        af=request.POST.get('aadhar_form')
        afo=request.POST.get('age_form')
        g=request.POST.get('gender')
        pnf=request.POST.get('pnumber_form')
        pef=request.POST.get('pemail_form')
        aform=request.POST.get('address_form')
        df=request.POST.get('disease_form')
        pdf=request.POST.get('P_Doctor_form')
        patient_model(pat_name=name,pat_aadhar=af,pat_age=afo,pat_gender=g,pat_phone_number=pnf,pat_email=pef,pat_address=aform,pat_disease=df,pat_doctor=pdf).save()
        return redirect("/patient_page/")

class staff_page(View):
    def get(sefl,request):
        data=staff_model.objects.all()
        context={"data":data}
        return render(request,"staff_page.html",context)
    
    def post(self,request):
        name=request.POST.get('name_form')
        email=request.POST.get('email_form')
        num=request.POST.get('number_form')
        pos=request.POST.get('position_form')
        dep=request.POST.get('department_form')
        jon=request.POST.get('joining_form')
        sal=request.POST.get('salary_form')
        staff_model(staff_name=name,staff_email=email,staff_phone=num,staff_role=pos,staff_department=dep,staff_hire=jon,staff_salary=sal).save()
        return redirect("/staff_page/")



        
class medicine_page(View):
    def get(sefl,request):
        data=medicine_model.objects.all()
        context={"data":data}
        return render(request,"medicine_page.html",context)
    
    def post(self,request):
        des=request.POST.get('description_form')
        df=request.POST.get('dose_form')
        sef=request.POST.get('seffect_form')
        sf=request.POST.get('storage_form')
        mdf=request.POST.get('mdate_form')
        ef=request.POST.get('edate_form')
        cf=request.POST.get('cost_form')
        medicine_model(med_descr=des,med_dose=df,med_side_effects=sef,med_storage=sf,med_mdate=mdf,med_edate=ef,med_cost=cf).save()
        return redirect("/medicine_page/")
