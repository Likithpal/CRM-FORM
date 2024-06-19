from django import forms
from .models import Guest
import re

class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = '__all__'
        widgets = {
            'bar_or_restaurant': forms.RadioSelect(choices=[('Bar', 'Bar'), ('Restaurant', 'Restaurant')]),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name.isalpha():
            raise forms.ValidationError("Name must contain only alphabetic characters.")
        return name

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not re.match(r'^\+?1?\d{10,15}$', phone):
            raise forms.ValidationError("Phone number must be entered in the format: '+999999999'")
        return phone

    def clean_table_no(self):
        table_no = self.cleaned_data.get('table_no')
        if not re.match(r'^\+?1?\d{1,100}$', table_no):
            raise forms.ValidationError("Table number must be numeric.")
        return table_no

   