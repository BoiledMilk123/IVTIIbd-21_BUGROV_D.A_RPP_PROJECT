from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Client, Employee, Branch, Service, Visit, VisitService
from .forms import RegisterForm

# Регистрация (без ограничений)
class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'visits/register.html'
    success_url = reverse_lazy('visit_list')

    def form_valid(self, form):
        user = form.save()
        return super().form_valid(form)

# Client CRUD
class ClientListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Client
    template_name = 'visits/client_list.html'
    context_object_name = 'clients'
    permission_required = 'visits.view_client'

class ClientDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Client
    template_name = 'visits/client_detail.html'
    context_object_name = 'client'
    permission_required = 'visits.view_client'

class ClientCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Client
    fields = ['full_name', 'email']
    template_name = 'visits/client_form.html'
    success_url = reverse_lazy('client_list')
    permission_required = 'visits.add_client'

class ClientUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Client
    fields = ['full_name', 'email']
    template_name = 'visits/client_form.html'
    success_url = reverse_lazy('client_list')
    permission_required = 'visits.change_client'

class ClientDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Client
    template_name = 'visits/client_confirm_delete.html'
    success_url = reverse_lazy('client_list')
    permission_required = 'visits.delete_client'

# Employee CRUD
class EmployeeListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Employee
    template_name = 'visits/employee_list.html'
    context_object_name = 'employees'
    permission_required = 'visits.view_employee'

class EmployeeDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Employee
    template_name = 'visits/employee_detail.html'
    context_object_name = 'employee'
    permission_required = 'visits.view_employee'

class EmployeeCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Employee
    fields = ['full_name', 'position']
    template_name = 'visits/employee_form.html'
    success_url = reverse_lazy('employee_list')
    permission_required = 'visits.add_employee'

class EmployeeUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Employee
    fields = ['full_name', 'position']
    template_name = 'visits/employee_form.html'
    success_url = reverse_lazy('employee_list')
    permission_required = 'visits.change_employee'

class EmployeeDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Employee
    template_name = 'visits/employee_confirm_delete.html'
    success_url = reverse_lazy('employee_list')
    permission_required = 'visits.delete_employee'

# Branch CRUD
class BranchListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Branch
    template_name = 'visits/branch_list.html'
    context_object_name = 'branches'
    permission_required = 'visits.view_branch'

class BranchDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Branch
    template_name = 'visits/branch_detail.html'
    context_object_name = 'branch'
    permission_required = 'visits.view_branch'

class BranchCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Branch
    fields = ['name', 'address']
    template_name = 'visits/branch_form.html'
    success_url = reverse_lazy('branch_list')
    permission_required = 'visits.add_branch'

class BranchUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Branch
    fields = ['name', 'address']
    template_name = 'visits/branch_form.html'
    success_url = reverse_lazy('branch_list')
    permission_required = 'visits.change_branch'

class BranchDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Branch
    template_name = 'visits/branch_confirm_delete.html'
    success_url = reverse_lazy('branch_list')
    permission_required = 'visits.delete_branch'

# Service CRUD
class ServiceListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Service
    template_name = 'visits/service_list.html'
    context_object_name = 'services'
    permission_required = 'visits.view_service'

class ServiceDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Service
    template_name = 'visits/service_detail.html'
    context_object_name = 'service'
    permission_required = 'visits.view_service'

class ServiceCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Service
    fields = ['name', 'description']
    template_name = 'visits/service_form.html'
    success_url = reverse_lazy('service_list')
    permission_required = 'visits.add_service'

class ServiceUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Service
    fields = ['name', 'description']
    template_name = 'visits/service_form.html'
    success_url = reverse_lazy('service_list')
    permission_required = 'visits.change_service'

class ServiceDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Service
    template_name = 'visits/service_confirm_delete.html'
    success_url = reverse_lazy('service_list')
    permission_required = 'visits.delete_service'

# VisitService CRUD
class VisitServiceListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = VisitService
    template_name = 'visits/visitservice_list.html'
    context_object_name = 'visitservices'
    permission_required = 'visits.view_visitservice'

class VisitServiceDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = VisitService
    template_name = 'visits/visitservice_detail.html'
    context_object_name = 'visitservice'
    permission_required = 'visits.view_visitservice'

class VisitServiceCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = VisitService
    fields = ['visit', 'service']
    template_name = 'visits/visitservice_form.html'
    success_url = reverse_lazy('visitservice_list')
    permission_required = 'visits.add_visitservice'

class VisitServiceUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = VisitService
    fields = ['visit', 'service']
    template_name = 'visits/visitservice_form.html'
    success_url = reverse_lazy('visitservice_list')
    permission_required = 'visits.change_visitservice'

class VisitServiceDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = VisitService
    template_name = 'visits/visitservice_confirm_delete.html'
    success_url = reverse_lazy('visitservice_list')
    permission_required = 'visits.delete_visitservice'

# Visit CRUD
class VisitListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Visit
    template_name = 'visits/visit_list.html'
    context_object_name = 'visits'
    permission_required = 'visits.view_visit'

class VisitDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Visit
    template_name = 'visits/visit_detail.html'
    context_object_name = 'visit'
    permission_required = 'visits.view_visit'

class VisitCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Visit
    fields = ['client', 'employee', 'branch', 'visit_date', 'visit_type']
    template_name = 'visits/visit_form.html'
    success_url = reverse_lazy('visit_list')
    permission_required = 'visits.add_visit'

class VisitUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Visit
    fields = ['client', 'employee', 'branch', 'visit_date', 'visit_type']
    template_name = 'visits/visit_form.html'
    success_url = reverse_lazy('visit_list')
    permission_required = 'visits.change_visit'

class VisitDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Visit
    template_name = 'visits/visit_confirm_delete.html'
    success_url = reverse_lazy('visit_list')
    permission_required = 'visits.delete_visit'