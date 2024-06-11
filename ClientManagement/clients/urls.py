from django.urls import path
from .views import login_view, clients_view, logout_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('clients/', clients_view, name='clients'),
    path('logout/', logout_view, name='logout'),
]
