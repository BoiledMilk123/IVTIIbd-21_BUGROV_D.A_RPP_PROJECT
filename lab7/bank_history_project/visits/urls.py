from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import TemplateView
from .views import (
    RegisterView,
    ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, ClientDeleteView,
    EmployeeListView, EmployeeDetailView, EmployeeCreateView, EmployeeUpdateView, EmployeeDeleteView,
    BranchListView, BranchDetailView, BranchCreateView, BranchUpdateView, BranchDeleteView,
    ServiceListView, ServiceDetailView, ServiceCreateView, ServiceUpdateView, ServiceDeleteView,
    VisitListView, VisitDetailView, VisitCreateView, VisitUpdateView, VisitDeleteView,
    VisitServiceListView, VisitServiceDetailView, VisitServiceCreateView, VisitServiceUpdateView, VisitServiceDeleteView
)
app_name = 'visits'

urlpatterns = [
    # Аутентификация
    path('login/', LoginView.as_view(template_name='visits/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    # Client URLs
    path('clients/', ClientListView.as_view(), name='client_list'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('clients/add/', ClientCreateView.as_view(), name='client_add'),
    path('clients/<int:pk>/edit/', ClientUpdateView.as_view(), name='client_edit'),
    path('clients/<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),
    # Employee URLs
    path('employees/', EmployeeListView.as_view(), name='employee_list'),
    path('employees/<int:pk>/', EmployeeDetailView.as_view(), name='employee_detail'),
    path('employees/add/', EmployeeCreateView.as_view(), name='employee_add'),
    path('employees/<int:pk>/edit/', EmployeeUpdateView.as_view(), name='employee_edit'),
    path('employees/<int:pk>/delete/', EmployeeDeleteView.as_view(), name='employee_delete'),
    # Branch URLs
    path('branches/', BranchListView.as_view(), name='branch_list'),
    path('branches/<int:pk>/', BranchDetailView.as_view(), name='branch_detail'),
    path('branches/add/', BranchCreateView.as_view(), name='branch_add'),
    path('branches/<int:pk>/edit/', BranchUpdateView.as_view(), name='branch_edit'),
    path('branches/<int:pk>/delete/', BranchDeleteView.as_view(), name='branch_delete'),
    # Service URLs
    path('services/', ServiceListView.as_view(), name='service_list'),
    path('services/<int:pk>/', ServiceDetailView.as_view(), name='service_detail'),
    path('services/add/', ServiceCreateView.as_view(), name='service_add'),
    path('services/<int:pk>/edit/', ServiceUpdateView.as_view(), name='service_edit'),
    path('services/<int:pk>/delete/', ServiceDeleteView.as_view(), name='service_delete'),
    # VisitService URLs
    path('visitservices/', VisitServiceListView.as_view(), name='visitservice_list'),
    path('visitservices/<int:pk>/', VisitServiceDetailView.as_view(), name='visitservice_detail'),
    path('visitservices/add/', VisitServiceCreateView.as_view(), name='visitservice_add'),
    path('visitservices/<int:pk>/edit/', VisitServiceUpdateView.as_view(), name='visitservice_edit'),
    path('visitservices/<int:pk>/delete/', VisitServiceDeleteView.as_view(), name='visitservice_delete'),
    # Visit URLs
    path('', VisitListView.as_view(), name='visit_list'),
    path('<int:pk>/', VisitDetailView.as_view(), name='visit_detail'),
    path('add/', VisitCreateView.as_view(), name='visit_add'),
    path('<int:pk>/edit/', VisitUpdateView.as_view(), name='visit_edit'),
    path('<int:pk>/delete/', VisitDeleteView.as_view(), name='visit_delete'),
    path('logout_success/', TemplateView.as_view(template_name='visits/logout_success.html'), name='logout_success'),
]