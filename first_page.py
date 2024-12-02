import logging
import asyncio
import os
import config
import keyboards as kb

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, FSInputFile
from dotenv import load_dotenv


# init

load_dotenv()
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()

# Получаем все медиа файлы из  директории с проектом (чтобы файлы корректно искались нга любой системе)

all_media_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'all_media_dir')


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет!', reply_markup=kb.main)


@dp.message(F.text == "О продукте")
async def about_info(message: Message):
    photo_file = FSInputFile(path=os.path.join(all_media_dir, 'sale.jpg'))
    await message.answer_photo(photo=photo_file, caption='О продукте')


@dp.message(F.text == "Часто задаваемые вопросы")
async def popular_questions(message: Message):
    await message.answer('Выбери вопрос', reply_markup=await kb.questions_keyboard())


# Обработка нажатий на вопросы
@dp.message(lambda message: message.text in config.questions.keys())
async def process_questions_button(message: Message):
    # Обработка нажатия кнопки
    if message.text == 'Назад':
        await message.answer(text=config.questions[message.text], reply_markup=kb.main)
    else:
        await message.answer(text=config.questions[message.text])


@dp.message(lambda message: message.text == 'Купить тетрадь' or 'Купить полную версию тетради')
async def buy_note(message: Message):
    if message.text == 'Купить тетрадь':
        link = config.note_link
        await message.answer(text=f'Тут должна быть ссылка на тетрадь\n{link}')
    elif message.text == 'Купить полную версию тетради':
        link = config.full_note_link
        await message.answer(text=f'Тут должна быть ссылка на полную тетрадь\n{link}')


#
# @dp.message(F.text == 'Купить полную версию тетради')
# async def buy_note(message: Message):
#     link = config.full_note_link
#     await message.answer(text=f'Тут должна быть ссылка на полную тетрадь\n{link}')


async def main():
    await dp.start_polling(bot, skip_updates=False)


if __name__ == "__main__":
    # log
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
