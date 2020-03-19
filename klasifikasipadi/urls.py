from django.urls import path
from klasifikasipadi import views

urlpatterns = [
    path('',views.pengujian, name="index"),
]