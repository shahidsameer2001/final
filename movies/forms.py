from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User


from .models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    INTERESTS = (
        ('python', 'Python'),
        ('java', 'Java'),
        ('c', 'C'),
        ('cpp', "C++"),
    )
    interests = forms.MultipleChoiceField(
        required=True,widget=forms.Select(), choices=INTERESTS)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2','interests']
        



class EditProfileForm(UserChangeForm):
    model = User
    fields = {
        'email',
        'username',
        'first_name',
        'last_name',
        'password'
    }


# for interest 

