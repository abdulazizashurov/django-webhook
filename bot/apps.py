import asyncio

from django.apps import AppConfig

from config import WEBHOOK_URL
from loader import bot


class BotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bot'

    def ready(self):
        loop = asyncio.get_event_loop()
        webhook_info = loop.run_until_complete(bot.get_webhook_info())
        if webhook_info.url != WEBHOOK_URL:
            loop.run_until_complete(bot.set_webhook(
                url=WEBHOOK_URL
            ))
