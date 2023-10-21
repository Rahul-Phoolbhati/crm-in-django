from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='base')
    path('home', views.home, name='homee'),
    # path('login/', views.login_, name='login')
    path('logout/', views.logout_, name='logoutt'),
    path('register/', views.register_, name='register'),
    path('add/', views.add, name='addd'),
    path('record/<int:pk>/', views.customer, name='records'),
    path('delete/<int:pk>/', views.delete__, name='delete'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),

]