from django import forms
from django.core.validators import RegexValidator
from django.forms import inlineformset_factory
from django.forms.widgets import CheckboxSelectMultiple

from koukoku.models import Estate, Image


class ImageUploadForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ['image']


class EstateCreationForm(forms.ModelForm):
    phone_message = 'Номер телефона должен быть в таком формате: 0555666999'

    phone_regex = RegexValidator(
        regex=r'^(0)\d{9}$',
        message=phone_message
    )
    phone = forms.CharField(validators=[phone_regex], max_length=10, label='Номер телефона')

    class Meta:
        model = Estate
        fields = ('name', 'description', 'plot_area', 'house_area', 'deal_type', 'price', 'currency',
                  'phone', 'location', 'target', 'communications', 'documents', 'infrastructure'
                  )
        widgets = {
            # 'images': forms.ClearableFileInput(attrs={'multiple': True}),
            'communications': CheckboxSelectMultiple(),
            'infrastructure': CheckboxSelectMultiple(),
        }


ImagesFormSet = inlineformset_factory(
    Estate,
    Image,
    form=ImageUploadForm,
    extra=0,
    can_delete=False,
    can_delete_extra=False,
)
