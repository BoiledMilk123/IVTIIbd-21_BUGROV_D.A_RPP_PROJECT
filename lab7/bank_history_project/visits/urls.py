from django.urls import path
from .views import VisitListView, VisitDetailView, VisitCreateView, VisitUpdateView, VisitDeleteView

urlpatterns = [
    path('', VisitListView.as_view(), name='visit_list'),
    path('<int:pk>/', VisitDetailView.as_view(), name='visit_detail'),
    path('add/', VisitCreateView.as_view(), name='visit_add'),
    path('<int:pk>/edit/', VisitUpdateView.as_view(), name='visit_edit'),
    path('<int:pk>/delete/', VisitDeleteView.as_view(), name='visit_delete'),
]
