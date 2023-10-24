from django.urls import path
from . import views

urlpatterns=[
    path('',views.getData,name="Read"),
    path('add/',views.addData,name="create"),
    path('update/<int:pk>',views.updateData,name="update"),
    path('delete/<int:pk>',views.deleteData,name="delete"),
   
]