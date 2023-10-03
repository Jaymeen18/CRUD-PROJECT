from django.core import validators
from django import forms
from .models import User


class Student_Registrations(forms.ModelForm):
    class Meta:
        model=User
        # fields=['name','email','password']
        fields='__all__'
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(render_value=True,attrs={'class':'form-control'}),

        }
        error_messages={
            'name':{'required':"Please Enter Your Name"},
            'email':{'required':"Please Enter Your Email"},
            'password':{'required':"Please Enter Your Password"},
        }
        
