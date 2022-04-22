from django.db import models


from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.db import models


class RegisterForm(UserCreationForm):
   
    first_name = forms.CharField(min_length=3, max_length=30, label = "First name", widget=forms.TextInput(attrs={'pattern':'[A-Za-ząćęłńóśźżĄĘŁŃÓŚŹŻ ]+', 'title':'Tylko litery [A-Z a-z ]', 'placeholder': 'Imię', 'class': 'form-control form-control-sm text-center rounded-0'}))
    last_name = forms.CharField(min_length=3, max_length=30, label = "Surname", widget=forms.TextInput(attrs={'pattern':'[A-Za-ząćęłńóśźżĄĘŁŃÓŚŹŻ ]+', 'title':'Tylko litery [A-Z a-z ]', 'placeholder': 'Nazwisko', 'class': 'form-control form-control-sm text-center rounded-0'}))
    email = forms.EmailField(label = "Email", widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control form-control-sm text-center rounded-0'}))

    username = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Login', 'class':'form-control form-control-sm text-center rounded-0'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Hasło', 'class':'form-control form-control-sm text-center rounded-0'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Hasło', 'class':'form-control form-control-sm text-center rounded-0'}))
 
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "username", "password1", "password2")

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        first_name = self.cleaned_data["first_name"]
        last_name = self.cleaned_data["last_name"]
        user.first_name = first_name
        user.last_name = last_name
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

