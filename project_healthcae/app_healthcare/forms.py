from django import forms
from .models import UserLoginModel
from .models import DiseaseModel,MedicineModel
import re


class  UserLoginForm(forms.ModelForm):

    gen=(
        ('Male','male'),
        ('Female','female'),
        ('other','other')
    )
    gender=forms.ChoiceField(choices=gen,widget=forms.RadioSelect)
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=UserLoginModel
        fields="__all__"

    def clean_firstname(self):
        fname=self.cleaned_data['firstname']
        res=re.match("^[A-Za-z]*$",fname)
        if res==None:
            raise forms.ValidationError("invalqwwid name")
        else:
            return fname
    def clean_lastname(self):
        lname=self.cleaned_data['firstname']
        res=re.match("^[A-Za-z]*$",lname)
        if res==None:
            raise forms.ValidationError("invalid name")
        else:
            return lname

class DiseaseForm(forms.ModelForm):
    class Meta:
        model=DiseaseModel
        fields="__all__"

class MedicineForm(forms.ModelForm):
    class Meta:
        model=MedicineModel
        fields="__all__"
        exclude = ("medcine_no",)