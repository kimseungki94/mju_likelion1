from django.contrib import admin
from django.urls import path
import blogprojectapp.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blogprojectapp.views.home,name="home"),
    path('<int:blog_id>',blogprojectapp.views.detail,name='detail'),
    path('new',blogprojectapp.views.new,name='new'),
    path('edit/<int:blog_id>',blogprojectapp.views.edit, name="edit"),
    path('delete/<int:blog_id>',blogprojectapp.views.delete, name="delete"),
    path('create',blogprojectapp.views.create, name='create'),
]
