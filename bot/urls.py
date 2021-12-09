from django.urls import path

from config import WEBHOOK_PATH
from .views import UpdateBot

urlpatterns = [
    path(WEBHOOK_PATH, UpdateBot.as_view()),

]
