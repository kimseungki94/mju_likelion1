from django.contrib import admin
from django.urls import path
import blog.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blog.views.home,name='home'),
    path('blog/<int:blog_id>',blog.views.detail,name='detail'),
    path('new',blog.views.new,name='new'),
    path('create',blog.views.create, name='create'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
