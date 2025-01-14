from .models import CustomUser
from django import forms

from django.contrib.auth.forms import UserCreationForm
from accounts.models import CustomUser,UserType



class RegisterForm(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput(
        render_value=True), label='Enter Password')
    password2 = forms.CharField(widget=forms.PasswordInput(
        render_value=True), label="Confirm Password")
    
    first_name = forms.CharField(required=True, label="First Name")
    last_name = forms.CharField(required=False, label="Last Name")
    email = forms.EmailField(required=True, label="Email Address")
    user_type = forms.ModelChoiceField(queryset=UserType.objects.all(), required=True, label='User Type')

    
    # level_master = forms.ModelMultipleChoiceField(queryset=UserType.objects.all(),
    #                                               required=False, label='Select levels', widget=forms.CheckboxSelectMultiple)

    
    class Meta:
        model = CustomUser
        fields = ['username', 'password1',
                  'password2', 'first_name', 'last_name', 'email',"age","user_type","profile_picture","bio","location","date_of_birth","interests","twitter_profile","instagram_profile","linkedin_profile"]