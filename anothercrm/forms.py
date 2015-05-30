from django.forms import ModelForm
from django.shortcuts import get_object_or_404

from .models import Relationship


class AddEmployeeForm(ModelForm):
    class Meta:
        model = Relationship
        fields = ('relatype', 'person')
