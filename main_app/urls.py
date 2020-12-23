from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('shtuff_lists/', views.ShtuffList.as_view(), name='shtuff_lists_index'),





]
