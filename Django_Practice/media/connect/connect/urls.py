from django.contrib import admin
from django.urls import path
import connectApp.views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', connectApp.views.home, name='home'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)