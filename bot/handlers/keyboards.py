from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

def get_keyboard(name: str):

    if name == 'start':
        keyboard = InlineKeyboardMarkup(resize_keyboard=True)
        keyboard.add(InlineKeyboardButton('Посмотреть', callback_data='look_auto'))
        keyboard.add(InlineKeyboardButton('Купить', callback_data='bay_auto'))
        keyboard.add(InlineKeyboardButton('Тех Потдержка', url='https://t.me/mb30ab'))
        keyboard.add(InlineKeyboardButton('Главное меню', callback_data='back'))
    elif name == 'look':
        keyboard = InlineKeyboardMarkup(resize_keyboard=True)
        keyboard.add(InlineKeyboardButton('Бренды', callback_data='cars'))
        keyboard.add(InlineKeyboardButton('Машины', callback_data='in_sale'))
        keyboard.add(InlineKeyboardButton('Главное меню', callback_data='back_look'))
    elif name == 'bay':
        keyboard = InlineKeyboardMarkup(resize_keyboard=True)
        keyboard.add(InlineKeyboardButton('В продаже', callback_data='on_sale'))
        keyboard.add(InlineKeyboardButton('Главное меню', callback_data='back_bay'))
        
    return keyboard

def get_keyboard_connect(name: str):
    if name == 'reservation':
        keyboard = InlineKeyboardMarkup(resize_keyboard=True)
        keyboard.add(InlineKeyboardButton('Забронировать', callback_data='reservation_auto'))
    elif name == 'connect':
        keyboard = InlineKeyboardMarkup(resize_keyboard=True)
        keyboard.add(InlineKeyboardButton('Заброн', url='https://t.me/mb30ab'))
        keyboard.add(InlineKeyboardButton('Главное меню', callback_data='back_conn'))
    
    return keyboard

# kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
# kb.add(KeyboardButton('Start'))