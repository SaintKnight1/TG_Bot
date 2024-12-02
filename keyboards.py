from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from config import questions

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


async def questions_keyboard():
    keyboard = ReplyKeyboardBuilder()
    questions_key_list = config.questions.keys()
    for question in questions_key_list:
        keyboard.add(KeyboardButton(text=question))
    return keyboard.as_markup().resize_keyboard
