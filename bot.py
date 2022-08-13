from googletrans import Translator
# print(tr.translate('siz yaxshimisiz?', dest = 'en'))
from buttons import til
import logging
import sqlite3
from api import API_TOKEN
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import CallbackQuery
from db import Sql
from datetime import datetime
import pytz


# country_time_zone = pytz.timezone('America/New_York')
# country_time = datetime.now(country_time_zone)
# print(country_time.strftime("Date is %d-%m-%y and time is %H:%M:%S"))



tr = Translator()

# Configure logging
logging.basicConfig(level=logging.INFO)

#Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)



x = Sql()

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
	x.baza_create()
    user_id = message.from_user.id
    username = message.from_user.username 
    first_name = message.from_user.first_name 
    y = x.user_check(user_id)
    if y is None:
        x.user_add(user_id, firstname, username)
        await bot.send_message(1813994648, f"User ID: {user_id}\nName: {firstname}\nUsername: @{username}")
        await message.answer("Assalamu alaykum \nHush kelibsiz!\nSiz bu bot orqali nafaqat tarjima \nbalki tarjima qilayotgan davlatingizni vaqtlarini ham ko'rish imkoniyati bor!")
        await message.answer("Marhamat so'z yoki matn kiriting!")
    else:
        await message.answer("Qaytganingiz bilan!\nSiz bu bot orqali nafaqat tarjima \nbalki tarjima qilayotgan davlatingizni vaqtlarini ham ko'rish imkoniyati bor!")
        await message.answer("Marhamat so'z yoki matn kiriting!" )



@dp.message_handler()
async def echo(message: types.Message):
	global t
	t = message.text
	await message.reply('Qaysi tilga tarjima qilmoqchisiz?', reply_markup = til)

@dp.callback_query_handler(text = "ru")
async def tarjima(call: CallbackQuery):

	country_time_zone = pytz.timezone('Europe/Moscow')
	country_time = datetime.now(country_time_zone)
	# print(country_time.strftime("Date is %d-%m-%y and time is %H:%M:%S"))
	tarjima = tr.translate(t, dest = "ru")
	await call.message.answer(country_time)
	await call.message.reply(tarjima.text)

@dp.callback_query_handler(text = "en")
async def tarjima(call: CallbackQuery):

	country_time_zone = pytz.timezone('America/New_York')
	country_time = datetime.now(country_time_zone)
	tarjima = tr.translate(t, dest = "en")
	await call.message.answer(country_time)
	await call.message.reply(tarjima.text)

@dp.callback_query_handler(text = "uz")
async def tarjima(call: CallbackQuery):

	country_time_zone = pytz.timezone('Asia/Tashkent')
	country_time = datetime.now(country_time_zone)
	tarjima = tr.translate(t, dest = "uz")
	await call.message.answer(country_time)
	await call.message.reply(tarjima.text)



@dp.callback_query_handler(text = "fr")
async def tarjima(call: CallbackQuery):

	country_time_zone = pytz.timezone('Europe/Paris')
	country_time = datetime.now(country_time_zone)
	tarjima = tr.translate(t, dest = "fr")
	await call.message.answer(country_time)
	await call.message.reply(tarjima.text)


@dp.callback_query_handler(text = "ar")
async def tarjima(call: CallbackQuery):

	country_time_zone = pytz.timezone('Asia/Dubai')
	country_time = datetime.now(country_time_zone)
	tarjima = tr.translate(t, dest = "ar")
	await call.message.answer(country_time)
	await call.message.reply(tarjima.text)


@dp.callback_query_handler(text = "zh-cn")
async def tarjima(call: CallbackQuery):

	country_time_zone = pytz.timezone('Asia/Shanghai')
	country_time = datetime.now(country_time_zone)
	tarjima = tr.translate(t, dest = "zh-cn")
	await call.message.answer(country_time)
	await call.message.reply(tarjima.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)