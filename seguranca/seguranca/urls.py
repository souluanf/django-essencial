from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('painel/', admin.site.urls),
]
