from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter


# urlpatterns=[
#     path('',views.getData,name="Read"),
#     path('add/',views.addData,name="create"),
#     path('update/<int:pk>',views.updateData,name="update"),
#     path('delete/<int:pk>',views.deleteData,name="delete"),
   
# ]

router = DefaultRouter()
router.register('crud',views.RecordViewSet,basename='user')

urlpatterns=[
    path("",include(router.urls))
]


# Now we can do crud operaioj through api
