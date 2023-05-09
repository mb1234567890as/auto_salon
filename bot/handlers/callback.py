import requests
from aiogram import types
from config import bot, dp, req_api
from .keyboards import get_keyboard, get_keyboard_connect
from config import text
from aiogram.utils.exceptions import MessageNotModified

async def look(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id = callback_query.message.message_id, text='Выберите действие', reply_markup=get_keyboard('look'))

async def bay(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id = callback_query.message.message_id, text='Выберите действие', reply_markup=get_keyboard('bay'))

async def cars(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    req = requests.get(f'{req_api}/api/car/').json()
    car = []
    for result in req:
        result = result['name']
        car.append(result)
    car = '\n\n'.join(car)
    await callback_query.message.answer(f'{car}')
    
async def create_car(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    reg = requests.get(f'{req_api}/createlist/').json()
    for result in reg:
        cleaned_result = {key: str(value).strip("'") for key, value in result.items()}
        await callback_query.message.answer('\n'.join(f'{key}: {value}' for key, value in cleaned_result.items()))

async def on_sale(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    reg = requests.get(f'{req_api}/createlist/').json()
    for result in reg:
        cleaned_result = {key: str(value).strip("'") for key, value in result.items()}
        await callback_query.message.answer('\n'.join(f'{key}: {value}' for key, value in cleaned_result.items()), reply_markup=get_keyboard_connect('reservation'))

async def back(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    # await bot.send_message(chat_id=callback_query.from_user.id, text='Главное меню', reply_markup=get_keyboard('start'))
    try:
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id = callback_query.message.message_id, text='Главное меню', reply_markup=get_keyboard('start'))
    except MessageNotModified:
        await bot.send_message(chat_id=callback_query.from_user.id, text="Сообщение не изменилось. Нет необходимости в обновлении.")


async def back_look(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    # await bot.send_message(chat_id=callback_query.from_user.id, text='Главное меню', reply_markup=get_keyboard('start'))
    try:
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id = callback_query.message.message_id, text='Главное меню', reply_markup=get_keyboard('start'))
    except MessageNotModified:
        await bot.send_message(chat_id=callback_query.from_user.id, text="Сообщение не изменилось. Нет необходимости в обновлении.")
async def back_bay(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    # await bot.send_message(chat_id=callback_query.from_user.id, text='Главное меню', reply_markup=get_keyboard('start'))
    try:
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id = callback_query.message.message_id, text='Главное меню', reply_markup=get_keyboard('start'))
    except MessageNotModified:
        await bot.send_message(chat_id=callback_query.from_user.id, text="Сообщение не изменилось. Нет необходимости в обновлении.")

async def back_conn(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    # await bot.send_message(chat_id=callback_query.from_user.id, text='Главное меню', reply_markup=get_keyboard('start'))
    try:
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id = callback_query.message.message_id, text='Главное меню', reply_markup=get_keyboard('start'))
    except MessageNotModified:
        await bot.send_message(chat_id=callback_query.from_user.id, text="Сообщение не изменилось. Нет необходимости в обновлении.")

async def connect(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id = callback_query.message.message_id, text=text, reply_markup=get_keyboard_connect('connect'))