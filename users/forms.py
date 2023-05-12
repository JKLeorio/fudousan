from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.validators import RegexValidator


class RegisterForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('email',)


class UserUpdateForm(forms.ModelForm):
    phone_message = 'Номер телефона должен быть в таком формате: 0555666999'

    phone_regex = RegexValidator(
        regex=r'^(0)\d{9}$',
        message=phone_message
    )
    phone = forms.CharField(validators=[phone_regex], max_length=10, label='Номер телефона')

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'phone', 'email', 'image')
