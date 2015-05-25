
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.core.urlresolvers import reverse_lazy

from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator

from .models import Company, Employee

#TODO: DRY !!!
class Index(TemplateView):
    template_name = 'index.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(Index, self).dispatch(*args, **kwargs)


class CompanyList(ListView):
    model = Company

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CompanyList, self).dispatch(*args, **kwargs)


class EmployeeList(ListView):
    model = Employee

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EmployeeList, self).dispatch(*args, **kwargs)


class CompanyDetail(DetailView):
    model = Company

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CompanyDetail, self).dispatch(*args, **kwargs)


class EmployeeDetail(DetailView):
    model = Employee 

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EmployeeDetail, self).dispatch(*args, **kwargs)


class CreateCompany(CreateView):
    template_name = 'anothercrm/create_form.html'
    model = Company
    fields = ('name', 'mission')

    @method_decorator(login_required)
    @method_decorator(permission_required('anothercrm.add_company'))
    def dispatch(self, *args, **kwargs):
        return super(CreateCompany, self).dispatch(*args, **kwargs)


class CreateEmployee(CreateView):
    template_name = 'anothercrm/create_form.html'
    model = Employee 
    fields = ('firstname', 'lastname', 'sex', 'company', 'position')

    @method_decorator(login_required)
    @method_decorator(permission_required('anothercrm.add_employee'))
    def dispatch(self, *args, **kwargs):
        return super(CreateEmployee, self).dispatch(*args, **kwargs)


class DeleteCompany(DeleteView):
    template_name = 'anothercrm/delete_form.html'
    model = Company
    success_url = reverse_lazy('anothercrm:company_list')

    @method_decorator(login_required)
    @method_decorator(permission_required('anothercrm.delete_company'))
    def dispatch(self, *args, **kwargs):
        return super(DeleteCompany, self).dispatch(*args, **kwargs)


class DeleteEmployee(DeleteView):
    template_name = 'anothercrm/delete_form.html'
    model = Employee 
    success_url = reverse_lazy('anothercrm:employee_list')

    @method_decorator(login_required)
    @method_decorator(permission_required('anothercrm.delete_employee'))
    def dispatch(self, *args, **kwargs):
        return super(DeleteEmployee, self).dispatch(*args, **kwargs)


class UpdateCompany(UpdateView):
    model = Company
    fields = ('name', 'mission')
    template_name = 'anothercrm/update_form.html'

    @method_decorator(login_required)
    @method_decorator(permission_required('anothercrm.change_company'))
    def dispatch(self, *args, **kwargs):
        return super(UpdateCompany, self).dispatch(*args, **kwargs)


class UpdateEmployee(UpdateView):
    model = Employee 
    fields = ('firstname', 'lastname', 'sex', 'company', 'position')
    template_name = 'anothercrm/update_form.html'

    @method_decorator(login_required)
    @method_decorator(permission_required('anothercrm.change_employee'))
    def dispatch(self, *args, **kwargs):
        return super(UpdateEmployee, self).dispatch(*args, **kwargs)
