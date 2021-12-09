from django.contrib import admin
from django.urls import path
from .views import UpdateBot

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<str:bot_token>/', UpdateBot.as_view()),
]
