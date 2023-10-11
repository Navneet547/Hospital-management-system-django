from django.db import models

# Create your models here.


#Doctor Moedel ------------------------->>>>>>>>>>>>>>>>>>>>>>>>
class doctor_model(models.Model):
    doc_name=models.CharField(max_length=40)
    doc_education=models.CharField(max_length=50)
    doc_phone_number=models.PositiveIntegerField()
    doc_specialization=models.CharField(max_length=50)
    doc_experience=models.CharField(max_length=50)
    # doc_id=models.PositiveIntegerField()
    # doc_email=models.EmailField(max_length=254)
    # doc_country=models.CharField(max_length=50)
    # doc_pass=models.PositiveIntegerField()
    


#Patient Moedel ------------------------->>>>>>>>>>>>>>>>>>>>>>>>

class patient_model(models.Model):
            pat_name=models.CharField(max_length=40)
            pat_aadhar=models.CharField(max_length=12)
            pat_age=models.CharField(max_length=5)
            pat_gender=models.CharField(max_length=10)
            pat_phone_number=models.PositiveIntegerField()
            pat_email=models.EmailField(max_length=40)
            pat_address=models.CharField(max_length=100)
            pat_disease=models.CharField(max_length=100)
            pat_doctor=models.CharField(max_length=50)
            # pat_allergies=


    # pat_allergies=enter some alergy


#Staff Moedel ------------------------->>>>>>>>>>>>>>>>>>>>>>>>

class staff_model(models.Model):
      staff_name=models.CharField(max_length=40)
      staff_email=models.EmailField(max_length=40)
      staff_phone=models.PositiveIntegerField()
      staff_role=models.CharField(max_length=40)
      staff_department=models.CharField(max_length=40)
      staff_hire=models.DateField()
      staff_salary=models.CharField(max_length=50)

#  Medicine Field------------------------>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class medicine_model(models.Model):
      med_descr=models.CharField(max_length=500)
      med_dose=models.CharField(max_length=200)
      med_side_effects=models.CharField(max_length=500)
      med_storage=models.CharField(max_length=100)
      med_mdate=models.DateField()
      med_edate=models.DateField()
      med_cost=models.PositiveIntegerField()