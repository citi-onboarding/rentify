from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class SignUpForm(forms.Form):
    username = forms.CharField(label='username',widget=forms.TextInput(attrs={'placeholder':'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'}))
    nationality = forms.CharField(max_length=50, required=True, help_text='Required. Just tell us from where you are', widget=forms.TextInput(
            attrs={
                'placeholder': 'Nationality',
            }))
    age = forms.IntegerField(required=False, help_text='Optional.', widget=forms.TextInput(
            attrs={
                'placeholder': 'Age',
            }))
    
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    gender = forms.ChoiceField(choices=GENDER, required=True)
    # profile = forms.ImageField()
    
    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )

    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'confirm_password', 'age', 'gender', 'nationality')

class SignInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)