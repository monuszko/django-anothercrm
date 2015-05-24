from django.conf.urls import url

from . import views


urlpatterns = (
        url(r'^$',
        views.Index.as_view(), name='index'),

        url(r'^companies/$',
        views.CompanyList.as_view(), name='company_list'),

        url(r'^employees/$',
        views.EmployeeList.as_view(), name='employee_list'),

        url(r'^company/(?P<name>[a-zA-Z0-9-]+)-(?P<pk>\d+)$',
        views.CompanyDetail.as_view(), name='company'),

        url(r'^employee/(?P<firstname>\w+)-(?P<lastname>[a-zA-Z-]+)-(?P<pk>\d+)$',
        views.EmployeeDetail.as_view(), name='employee'),

        url(r'^create/company$',
        views.CreateCompany.as_view(), name='create_company'),

        url(r'^create/employee$',
        views.CreateEmployee.as_view(), name='create_employee'),

        url(r'^delete/company/(?P<pk>\d+)$',
        views.DeleteCompany.as_view(), name='delete_company'),

        url(r'^delete/employee/(?P<pk>\d+)$',
        views.DeleteEmployee.as_view(), name='delete_employee'),

        url(r'^update/company/(?P<pk>\d+)$',
        views.UpdateCompany.as_view(), name='update_company'),

        url(r'^update/employee/(?P<pk>\d+)$',
        views.UpdateEmployee.as_view(), name='update_employee'),
        )


