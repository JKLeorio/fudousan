from django import forms

from koukoku.models import Region, City, District, Communication, Estate


class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = ('name',)


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ('name', 'region')


class DistrictForm(forms.ModelForm):
    class Meta:
        model = District
        fields = ('name', 'city')


class CommunicationForm(forms.ModelForm):
    class Meta:
        model = Communication
        fields = ('name',)


class EstateForm(forms.ModelForm):
    class Meta:
        model = Estate
        fields = ('name', 'description', 'image', 'plot_area', 'house_area', 'deal_type', 'price', 'currency', 'phone',
                  'location', 'target', 'communications', 'documents', 'infrastructure', 'payment_term',
                  )
