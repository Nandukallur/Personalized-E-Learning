from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class RegForm(UserCreationForm):
    class Meta:
        model=CustUser
        fields=['username','email','first_name','last_name','password1','password2']
    username=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Username","class":"form-control","style":"border-radius: 0.75rem; "}))
    email=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Email","class":"form-control","style":"border-radius: 0.75rem; "}))
    first_name=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"First Name","class":"form-control","style":"border-radius: 0.75rem; "}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Last Name","class":"form-control","style":"border-radius: 0.75rem; "}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Password","class":"form-control","style":"border-radius: 0.75rem; "}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Confirm Password","class":"form-control","style":"border-radius: 0.75rem; "}))       
    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     if CustUser.objects.filter(email=email).exists():
    #         raise forms.ValidationError("The Email is already in use. Please use a different email")

    #     if not email.endswith('@example.com'):
    #         raise forms.ValidationError("Please use a valid email ending with @example.com")
    #     return email
    def clean_password2(self):
        password1=self.cleaned_data.get('password1')
        password2=self.cleaned_data.get('password2')
        if password1 and password2 and password1!=password2:
            raise forms.ValidationError('Password Does Not Match')
        
        min_length=8
        if len(password2)<min_length:
            raise forms.ValidationError(f"Password must be atlease {min_length} characters long")
        return super().clean_password2()

    

class LoginForm(forms.Form):
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Username"}))        
    password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password","name":"password"}))    



class ChangePasswordForm(forms.Form):
    current_password=forms.CharField(max_length=50,label="current password",widget=forms.PasswordInput(attrs={"placeholder":"Current Password","class":"form-control"}))
    new_password=forms.CharField(max_length=50,label="new password",widget=forms.PasswordInput(attrs={"placeholder":"New Password","class":"form-control"}))
    confirm_password=forms.CharField(max_length=50,label="confirm password",widget=forms.PasswordInput(attrs={"placeholder":"Confirm Password","class":"form-control"}))



class StudentFormProfile(forms.ModelForm):
     class Meta:
          model=CustUser
          fields=['first_name','last_name','email','gender','age']
          widgets={
               'first_name':forms.TextInput(attrs={"placeholder":"Firstname","class":"form-control","style":"border-radius: 0.75rem; "}),
               'last_name':forms.TextInput(attrs={"placeholder":"Lastname","class":"form-control","style":"border-radius: 0.75rem; "}),
               'email':forms.TextInput(attrs={"placeholder":"Email","class":"form-control","style":"border-radius: 0.75rem; "}),
               'gender':forms.RadioSelect(),
               'age':forms.NumberInput(attrs={"placeholder":"Age","class":"form-control","style":"border-radius: 0.75rem; "}),
          }








class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
            'message': forms.Textarea(attrs={'placeholder': 'Enter your feedback'}),
        }
