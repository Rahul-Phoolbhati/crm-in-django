from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='base')
    path('home', views.home, name='homee'),
    # path('login/', views.login_, name='login')
    path('logout/', views.logout_, name='logoutt'),
    path('register/', views.register_, name='register')
]