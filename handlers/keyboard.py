from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup

mainmenu_aboutus = KeyboardButton('О нас')
mainmenu_help = KeyboardButton('Помощь')
mainmenu = ReplyKeyboardMarkup(resize_keyboard=True).row(mainmenu_help, mainmenu_aboutus)

help = InlineKeyboardMarkup(row_width=2)
help_finance = InlineKeyboardButton(text='Финансовая', callback_data='helpfinance')
help_physically = InlineKeyboardButton(text='Физическая', callback_data='helpphysically')

help.insert(help_finance)
help.insert(help_physically)