from . import views
from django.urls import path

urlpatterns = [
    path('',views.demo, name='demo'),
    path('team', views.demo, name='demo'),
    #path('operations/', views.operations, name='operations'),
    #path('contact/',views.contact, name='contact')

]
