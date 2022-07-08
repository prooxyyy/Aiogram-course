from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from configure import cfg

storage = MemoryStorage()
bot = Bot(token=cfg['token'])
dp = Dispatcher(bot, storage=storage)