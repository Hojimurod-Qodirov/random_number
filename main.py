import logging
import random
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor

API_TOKEN = '6460684839:AAHps-3sFzzDuDdb4SPiLfdvAjvri83zS7M'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
database = []


@dp.message_handler(commands=['start'])
async def start_game(message: types.Message):
    user_id = message.from_user.id
    database[user_id] = {
        'taxmin': 0,
        'son': random.randint(1, 100)
    }
    await message.reply("Keling o'ylangan son topish o'yinini o'ynaymi")


@dp.message_handler(lambda message: message.text.isdigit() and int(message.text) > 0, content_types=types.ContentTypes.TEXT)
async def guess_number(message: types.Message):
    user_id = message.from_user.id
    if user_id not in database:
        await message.reply("oyinni boshlash uchun /start ni bosing.")
        return

    database[user_id]['taxmin'] += 1
    javob = int(message.text)
    r = database[user_id]['son']

    if javob == r:
        await message.reply(f"Topdingiz men {r} sonini o'ylagandim, shuncha  taxmin qildiz {database[user_id]['taxmin']}.")
        del database[user_id]
    elif javob < r:
        await message.reply("Xato! Men o'ylagan son bundan kattaroq:")
    else:
        await message.reply("Xato! Men o'ylagan son bundan kichikroq:")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
