from bot import dp, bot
from aiogram.utils import executor
from handlers import client

client.register_client()

executor.start_polling(dp, skip_updates=True)