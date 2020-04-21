from django.db import models

class UserLoginModel(models.Model):
    idno=models.IntegerField(primary_key=True)
    firstname=models.CharField(max_length=40)
    lastname=models.CharField(max_length=30)
    age=models.IntegerField()
    gender=models.CharField(max_length=15)
    address=models.CharField(max_length=200)
    usermname=models.EmailField(unique=True)
    password=models.CharField(max_length=10)

class DiseaseModel(models.Model):
    des_name=models.CharField(max_length=40)
    des_sym=models.CharField(max_length=40)

    def __str__(self):
        return self.des_name

class MedicineModel(models.Model):
    medcine_no=models.IntegerField(primary_key=True)
    medcine_name=models.CharField(max_length=60)
    medcine_description=models.CharField(max_length=60)
    disease=models.ForeignKey(DiseaseModel,on_delete=models.CASCADE)
