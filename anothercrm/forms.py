from django.forms import ModelForm
from django.shortcuts import get_object_or_404

from .models import Relationship, Trade, Company, Person


class AddEmployeeForm(ModelForm):
    class Meta:
        model = Relationship
        fields = ('relatype', 'person')


class AddTradeForm(ModelForm):
    class Meta:
        model = Trade
        fields = ('name',)


class AddCompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'mission', 'trades')


class AddPersonForm(ModelForm):
    class Meta:
        model = Person
        fields = (
                'firstname',
                'lastname',
                'sex',
                'email',
                'mobile',
                'address',
                'zipcode',
                'city',
                'state',
                'country'
                )
