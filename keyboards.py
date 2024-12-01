from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='О продукте')],
    [KeyboardButton(text='Часто задаваемые вопросы')],
    [KeyboardButton(text='Купить тетрадь'), KeyboardButton(text='Купить полную версию тетради')]
],
    resize_keyboard=True,
    input_field_placeholder='Выбери пункт меню.')

questions_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вопрос 1')],
    [KeyboardButton(text='Вопрос 2')],
    [KeyboardButton(text='Вопрос 3')],
    [KeyboardButton(text='Назад')]
],
    resize_keyboard=True,
    input_field_placeholder='Выбери пункт меню.')
