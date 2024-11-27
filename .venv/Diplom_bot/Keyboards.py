from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InputFile
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Подбор"),
            KeyboardButton(text="О нас")
        ]
    ], resize_keyboard=True
)

podbor_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Новичок", callback_data="New")],
        [InlineKeyboardButton(text="Прогрессирующий", callback_data="Medium")],
        [InlineKeyboardButton(text="Профи", callback_data="Pro")],
        [InlineKeyboardButton(text="Помощь", callback_data="other")]
    ], resize_keyboard=True
)

progress_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Универсальный", callback_data="Universal")],
        [InlineKeyboardButton(text="Фристайл", callback_data="Freestyle")],
        [InlineKeyboardButton(text="Фрирайд", callback_data="Freeride")],
    ], resize_keyboard=True
)

profy_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Универсальный", callback_data="ProUniversal")],
        [InlineKeyboardButton(text="Фристайл", callback_data="ProFreestyle")],
        [InlineKeyboardButton(text="Фрирайд", callback_data="ProFreeride")],
    ], resize_keyboard=True
)

buy_kb = InlineKeyboardMarkup(
    inline_keyboard=[
    [InlineKeyboardButton(text="Купить", url = "http://ya.ru")],
    [InlineKeyboardButton(text="Назад", callback_data="back_to_cataloge")]
    ]
)