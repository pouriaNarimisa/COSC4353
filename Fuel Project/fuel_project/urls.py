
from django.contrib import admin
from django.urls import include, path

from fuel_app import views

urlpatterns = [
    path('', include('fuel_app.urls')),
    path('admin/', admin.site.urls),
]
