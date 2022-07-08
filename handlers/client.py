from aiogram import types

from bot import dp, bot
from handlers import keyboard
from others.db import Database

async def start(message: types.Message):
    try:
        await message.answer('Бот работает!', reply_markup=keyboard.mainmenu)
    except Exception as e:
        print(e)

async def database_learning(message: types.Message):
    try:
        db = Database()

        db.remove('users', "nickname = 'test'")
        await message.answer('deleted!')
    except Exception as e:
        print(e)

async def keyboard_handler(message: types.Message):
    try:
        match message.text:
            case "Помощь":
                await message.reply('Какая тебе нужна помощь, друг?', reply_markup=keyboard.help)
            case "О нас":
                await message.reply('Этот бот сделан для обучения библиотеки Aiogram')
            case _:
                await message.answer('Такой команды не существует!')
    except Exception as e:
        print(e)

async def inline_help_buttons_handler(call: types.CallbackQuery):
    match call.data:
        case "helpfinance":
            await call.message.answer("Финансовая помощь не доступна!")
            await bot.answer_callback_query(callback_query_id=call.id)
        case "helpphysically":
            await call.message.answer("Физическая помощь не доступна!")
            await bot.answer_callback_query(callback_query_id=call.id)

def register_client():
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(database_learning, commands='dbtest')
    dp.register_message_handler(keyboard_handler, state=None)
    dp.register_callback_query_handler(inline_help_buttons_handler)