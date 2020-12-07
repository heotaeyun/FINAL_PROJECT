from django.contrib.auth.forms import UserChangeForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django import forms

class CustomUserChangeForm(UserChangeForm):
    username = forms.CharField(
    label  = '',
    widget = forms.TextInput(attrs={
        'class'       : 'form-control',
        'placeholder' : '아이디를 입력해주세요',
        })
    )
    class Meta:
        model  = get_user_model()
        fields = ('username',)


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
    label  = '',
    widget = forms.TextInput(attrs={
        'class'       : 'form-control',
        'placeholder' : '가입하실 아이디를 입력해주세요',
        })
    )
    password1 = forms.CharField(
    label  = '',
    widget = forms.PasswordInput(attrs={
        'class'       : 'form-control',
        'placeholder' : '가입하실 비밀번호를 입력해주세요',
        })
    )
    password2 = forms.CharField(
    label  = '',
    widget = forms.PasswordInput(attrs={
        'class'       : 'form-control',
        'placeholder' : '가입하실 비밀번호를 확인해주세요',      
        })
    )
    class Meta(UserCreationForm.Meta):
        model  = get_user_model()
        fields = UserCreationForm.Meta.fields


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
    label  = '',
    widget = forms.TextInput(attrs={
        'class'       : 'form-control',
        'placeholder' : '아이디를 입력해주세요',
        })
    )
    password = forms.CharField(
    label  = '',
    widget = forms.PasswordInput(attrs={
        'class'       : 'form-control',
        'placeholder' : '비밀번호를 입력해주세요',
        })
    )
    class Meta:
        model  = get_user_model()
        fields = ('username', 'password1',)

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
    label  = '예전 비밀번호',
    widget = forms.PasswordInput(attrs={
        'class'       : 'password-control',
        'placeholder' : '예전 비밀번호를 확인해주세요',  
        })
    )
    new_password1 = forms.CharField(
    label  = '새로운 비밀번호',
    widget = forms.PasswordInput(attrs={
        'class'       : 'password-control',
        'placeholder' : '새로운 비밀번호를 확인해주세요',        
        })
    )
    new_password2 = forms.CharField(
    label  = '새로운 비밀번호2',
    widget = forms.PasswordInput(attrs={
        'class'       : 'password-control',
        'placeholder' : '새로운 비밀번호를 확인해주세요',
        })
    )
    class Meta:
        model  = get_user_model()
        fields = ('old_password', 'new_password1', 'new_password2')