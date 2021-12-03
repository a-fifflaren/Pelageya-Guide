# import markups as nav  # Подключения кнопак меню
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.utils import executor
from config import BOT_TOKEN  # Подключения api токена

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id,
                           "Добро пожаловать {0.first_name}!\nМеня зовут Пелагея! Я твой гид по Выборгу.")


@dp.message_handler(commands=['eat'])
async def command_eat(message: types.Message):
    await bot.send_message(message.from_user.id, "Скоро мы добавим вкусные места!")


if __name__ == '__main__':
    executor.start_polling(dp)
