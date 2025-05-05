from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Visit

class VisitListView(ListView):
    model = Visit
    template_name = 'visits/visit_list.html'
    context_object_name = 'visits'

class VisitDetailView(DetailView):
    model = Visit
    template_name = 'visits/visit_detail.html'
    context_object_name = 'visit'

class VisitCreateView(CreateView):
    model = Visit
    fields = ['client', 'employee', 'branch', 'visit_date', 'visit_type']
    template_name = 'visits/visit_form.html'
    success_url = reverse_lazy('visit_list')

class VisitUpdateView(UpdateView):
    model = Visit
    fields = ['client', 'employee', 'branch', 'visit_date', 'visit_type']
    template_name = 'visits/visit_form.html'
    success_url = reverse_lazy('visit_list')

class VisitDeleteView(DeleteView):
    model = Visit
    template_name = 'visits/visit_confirm_delete.html'
    success_url = reverse_lazy('visit_list')

