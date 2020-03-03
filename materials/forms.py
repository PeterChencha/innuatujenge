from .models import *
from django.forms import ModelForm
from django import forms
from django.contrib.admin import widgets
from django.contrib.admin.widgets import AdminDateWidget
from .widgets import BootstrapDateTimePickerInput


class MaterialDeliveryForm(ModelForm):

    date_received = forms.DateField(
        widget=forms.DateInput(
        attrs={'type': 'date'},
        )
    )

    time_received = forms.TimeField(
        widget=forms.TimeInput(
        attrs={'type': 'time'},
        )
    )
    class Meta:
        model = Materials
        fields = ['house_id', 'item_name', 'date_received', 'time_received', 'quantity', 'item_unit']
