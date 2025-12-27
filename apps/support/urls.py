from django.urls import path
from . import views

app_name = 'support'

urlpatterns = [
    path('ticket/new/', views.TicketCreateView.as_view(), name='ticket_create'),
    path('ticket/<int:pk>/', views.TicketDetailView.as_view(), name='ticket_detail'),
]
