from django.contrib import admin
from django.urls import path
import connectApp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', connectApp.views.home, name='home'),
]