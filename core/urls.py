from django.urls import path

from . import views

urlpatterns = [
    path('add_shift/',views.Add_shift_view.as_view(), name='Add_shift_view'),
    path('seven_day/',views.Seven_day_view.as_view(), name='Seven_day_view'),
    path('add_staff/',views.Add_staff_member.as_view(), name='Add_staff_view'),
    path('staff_list/',views.Staff_list_view.as_view(), name='Staff_list_view'),
    path('staff_list/<int:pk>/', views.Staff_lookup_view.as_view(), name='Staff_lookup_view'),
    path('multiple_shifts_success/', views.Staff_lookup_view.as_view(), name='Add_multiple'),
    path('', views.Index.as_view(), name="index"),
]
