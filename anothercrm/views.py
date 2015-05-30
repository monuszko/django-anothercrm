
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, get_object_or_404

from .models import Company, Person
from .forms import AddEmployeeForm

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


class PersonList(ListView):
    model = Person

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PersonList, self).dispatch(*args, **kwargs)


class PersonDetail(DetailView):
    model = Person 

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PersonDetail, self).dispatch(*args, **kwargs)


class CreateCompany(CreateView):
    template_name = 'anothercrm/create_form.html'
    model = Company
    fields = ('name', 'mission')

    @method_decorator(login_required)
    @method_decorator(permission_required('anothercrm.add_company'))
    def dispatch(self, *args, **kwargs):
        return super(CreateCompany, self).dispatch(*args, **kwargs)


class CreatePerson(CreateView):
    template_name = 'anothercrm/create_form.html'
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

    @method_decorator(login_required)
    @method_decorator(permission_required('anothercrm.add_employee'))
    def dispatch(self, *args, **kwargs):
        return super(CreatePerson, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        return self.request.GET.get('origin') or self.object.get_absolute_url()


class DeleteCompany(DeleteView):
    template_name = 'anothercrm/delete_form.html'
    model = Company
    success_url = reverse_lazy('anothercrm:company_list')

    @method_decorator(login_required)
    @method_decorator(permission_required('anothercrm.delete_company'))
    def dispatch(self, *args, **kwargs):
        return super(DeleteCompany, self).dispatch(*args, **kwargs)


class DeletePerson(DeleteView):
    template_name = 'anothercrm/delete_form.html'
    model = Person 
    success_url = reverse_lazy('anothercrm:employee_list')

    @method_decorator(login_required)
    @method_decorator(permission_required('anothercrm.delete_employee'))
    def dispatch(self, *args, **kwargs):
        return super(DeletePerson, self).dispatch(*args, **kwargs)


class UpdateCompany(UpdateView):
    model = Company
    fields = ('name', 'mission')
    template_name = 'anothercrm/update_form.html'

    @method_decorator(login_required)
    @method_decorator(permission_required('anothercrm.change_company'))
    def dispatch(self, *args, **kwargs):
        return super(UpdateCompany, self).dispatch(*args, **kwargs)


class UpdatePerson(UpdateView):
    model = Person 
    fields = ('firstname', 'lastname', 'sex', 'company', 'position')
    template_name = 'anothercrm/update_form.html'

    @method_decorator(login_required)
    @method_decorator(permission_required('anothercrm.change_employee'))
    def dispatch(self, *args, **kwargs):
        return super(UpdatePerson, self).dispatch(*args, **kwargs)


@login_required
@permission_required('anothercrm.change_employee')
def company_detail(request, name, pk):
    company = get_object_or_404(Company, pk=pk)
    if request.method == 'POST':
        form = AddEmployeeForm(request.POST)
        if form.is_valid():
            new_employee = form.save(commit=False)
            new_employee.company = company
            new_employee.save()
            return HttpResponseRedirect(request.path)
    else:
        form = AddEmployeeForm()

    return render(request, 'anothercrm/company_detail.html', {'form': form,
                                                              'company': company,
                                                             })

