
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('website/',include('website.urls')),
    # path('api/',include('api.urls')),
    path('api/',include('website.api.urls'))
]
