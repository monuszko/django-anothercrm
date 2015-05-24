
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.core.urlresolvers import reverse_lazy

from .models import Company, Employee


class Index(TemplateView):
    template_name = 'index.html'


#TODO: login_required
class CompanyList(ListView):
    model = Company


class EmployeeList(ListView):
    model = Employee


class CompanyDetail(DetailView):
    model = Company


class EmployeeDetail(DetailView):
    model = Employee 


class CreateCompany(CreateView):
    template_name = 'anothercrm/create_form.html'
    model = Company
    fields = ('name', 'mission')


class CreateEmployee(CreateView):
    template_name = 'anothercrm/create_form.html'
    model = Employee 
    fields = ('firstname', 'lastname', 'sex', 'company', 'position')


class DeleteCompany(DeleteView):
    template_name = 'anothercrm/delete_form.html'
    model = Company
    success_url = reverse_lazy('anothercrm:company_list')


class DeleteEmployee(DeleteView):
    template_name = 'anothercrm/delete_form.html'
    model = Employee 
    success_url = reverse_lazy('anothercrm:employee_list')


class UpdateCompany(UpdateView):
    model = Company
    fields = ('name', 'mission')
    template_name = 'anothercrm/update_form.html'


class UpdateEmployee(UpdateView):
    model = Employee 
    fields = ('firstname', 'lastname', 'sex', 'company', 'position')
    template_name = 'anothercrm/update_form.html'
