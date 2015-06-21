from django.conf.urls import url

from django.core.urlresolvers import reverse_lazy
from . import views
from .models import Company, Trade
from .forms import AddTradeForm, AddCompanyForm, AddPersonForm


urlpatterns = (
        url(r'^$',
        views.Index.as_view(), name='index'),

        url(r'^companies/$',
        views.CompanyList.as_view(), name='company_list'),

        url(r'^persons/$',
        views.PersonList.as_view(), name='person_list'),

        url(r'^company/(?P<name>[a-zA-Z0-9-]+)-(?P<pk>\d+)$',
        views.company_detail, name='company'),

        url(r'^person/(?P<firstname>\w+)-(?P<lastname>[a-zA-Z-]+)-(?P<pk>\d+)$',
        views.PersonDetail.as_view(), name='person'),

        url(r'^create/company$',
            views.create_object, {'form': AddCompanyForm}, name='create_company'),

        url(r'^create/person$',
            views.create_object, {'form': AddPersonForm}, name='create_person'),

        url(r'^create/trade$',
            views.create_object, {'form': AddTradeForm}, name='create_trade'),

        url(r'^delete/company/(?P<pk>\d+)$',
            views.delete_object, {'model': Company}, name='delete_company'),


        url(r'^delete/person/(?P<pk>\d+)$',
        views.DeletePerson.as_view(), name='delete_person'),

        url(r'^update/company/(?P<pk>\d+)$',
        views.UpdateCompany.as_view(), name='update_company'),

        url(r'^update/person/(?P<pk>\d+)$',
        views.UpdatePerson.as_view(), name='update_person'),
        )


