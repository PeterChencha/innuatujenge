from .models import *
from django.forms import ModelForm
from django import forms
from django.contrib.admin import widgets
from django.contrib.admin.widgets import AdminDateWidget

class MaterialDeliveryForm(ModelForm):

    date_received = forms.DateTimeField(widget=AdminDateWidget())
    class Meta:
        model = Materials
        fields = ['house_id', 'item_name', 'date_received', 'quantity', 'item_unit']