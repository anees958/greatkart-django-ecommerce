from turtle import width
from django import forms

from account.models import Account

class RegistrationForm(forms.ModelForm):

    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password',
        'class': 'form-control',
    }))

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password',
        'class': 'form-control',
    }))

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']

         



         # This Function will check password is matched with confirm password during registration

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(

                "Password does not match!"
                ) 

         # This Function Will Provide Bootstarp Form control to all fields

    def __init__(self,*args,**kwargs):
             super(RegistrationForm,self).__init__(*args,**kwargs)
             self.fields['first_name'].widget.attrs['placeholder']='Enter First Name'
             self.fields['last_name'].widget.attrs['placeholder'] = 'Enter last Name'
             self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter Phone Number'
             self.fields['email'].widget.attrs['placeholder'] = 'Enter Email Address'

             for field in self.fields:
                 self.fields[field].widget.attrs['class']='form-control'


        
         