from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='О продукте')],
    [KeyboardButton(text='Купить тетрадь'), KeyboardButton(text='Купить полную версию тетради')]
],
    resize_keyboard=True,
    input_field_placeholder='Выбери пункт меню.')