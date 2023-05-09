import psycopg2
from aiogram import types
from aiogram.utils import executor
from config import bot, dp, req_api
from handlers.keyboards import *
from handlers.callback import *
from psycopg2 import Error

import requests





@dp.message_handler(commands='start')
async def start_prod(message: types.Message):
    await bot.send_message(chat_id= message.from_user.id, text='Вздраствуйте, Добро пожаловать в наш салон!', reply_markup=get_keyboard('start'))
    

@dp.callback_query_handler(lambda callback : callback.data == 'look_auto')
async def process_look(callback_query : types.CallbackQuery):
    await look(callback_query)

@dp.callback_query_handler(lambda callback : callback.data == 'bay_auto')
async def process_bay(callback_query : types.CallbackQuery):
    await bay(callback_query)


@dp.callback_query_handler(lambda callback : callback.data == 'cars')
async def process_cars(callback_query : types.CallbackQuery):
    await cars(callback_query)


@dp.callback_query_handler(lambda callback : callback.data == 'back')
async def process_back(callback_query : types.CallbackQuery):
    await back(callback_query)

@dp.callback_query_handler(lambda callback : callback.data == 'in_sale')
async def process_create_car(callback_query : types.CallbackQuery):
    await create_car(callback_query)

@dp.callback_query_handler(lambda callback : callback.data == 'on_sale')
async def process_create_car(callback_query : types.CallbackQuery):
    await on_sale(callback_query)

@dp.callback_query_handler(lambda callback : callback.data == 'back_look')
async def process_back(callback_query : types.CallbackQuery):
    await back_look(callback_query)

@dp.callback_query_handler(lambda callback : callback.data == 'back_bay')
async def process_back(callback_query : types.CallbackQuery):
    await back_bay(callback_query)

@dp.callback_query_handler(lambda callback : callback.data == 'back_conn')
async def process_back(callback_query : types.CallbackQuery):
    await back_conn(callback_query)
 

@dp.callback_query_handler(lambda callback : callback.data == 'reservation_auto')
async def process_back(callback_query : types.CallbackQuery):
    await connect(callback_query)

if __name__ == '__main__':
    print('start bot...')
    executor.start_polling(dp, skip_updates=True)


