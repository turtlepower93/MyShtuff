from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('shtuff_lists/', views.ShtuffListList.as_view(), name='shtuff_lists_index'),
    path('shtuff_lists/create/', views.ShtuffListCreate.as_view(), name='shtuff_list_create'),
    path('shtuff_lists/<int:pk>/delete/', views.ShtuffListDelete.as_view(), name='shtuff_list_delete'),
    path('shtuff_lists/<int:pk>/update/', views.ShtuffListUpdate.as_view(), name='shtuff_list_update'),
    path('shtuff_lists/<int:shtuff_list_id>/', views.shtuff_list_detail, name='shtuff_list_detail'),

    path('shtuff/<int:pk>/create/', views.ShtuffCreate.as_view(), name="shtuff_create"),
    path('shtuff/<int:pk>/delete/', views.ShtuffDelete.as_view(), name="shtuff_delete"),
    path('shtuff/<int:pk>/update/', views.ShtuffUpdate.as_view(), name="shtuff_update"),
    path('shtuff/<int:shtuff_id>/', views.shtuff_detail, name="shtuff_detail"),

]
