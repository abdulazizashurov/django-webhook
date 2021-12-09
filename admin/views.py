import asyncio
from aiogram import types, Dispatcher, Bot, bot
from rest_framework.response import Response
from rest_framework.views import APIView
from handler import dp
from config import WEBHOOK_URL
from loader import bot
print(dp.bot)

loop = asyncio.get_event_loop()


def on_start():
    webhook_info = loop.run_until_complete(bot.get_webhook_info())
    if webhook_info.url != WEBHOOK_URL:
        loop.run_until_complete(bot.set_webhook(
            url=WEBHOOK_URL
        ))


class UpdateBot(APIView):
    def post(self, request):
        try:
            update = types.Update(**request.data)
            Dispatcher.set_current(dp)
            Bot.set_current(dp.bot)
            loop.run_until_complete(dp.process_update(update))
        except Exception as e:
            print(e)
        finally:
            return Response(status=200)




