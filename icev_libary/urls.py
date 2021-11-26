from django.contrib import admin
from django.urls import path
from libary.views import *


urlpatterns = [
  path('admin/', admin.site.urls),
  path('', home, name="home"),
  path('register/', register, name="register"),
  path('edit/<int:id>/', edit, name="edit"),
  path('delete/<int:id>/', delete, name="delete"),
]
