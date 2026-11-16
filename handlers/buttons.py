from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

main_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='/start'), KeyboardButton(text='/mem')]
    ],
    resize_keyboard=True
)

menu_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Мем', callback_data='mem')]
    ]
)

edit_fields = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Название', callback_data='field_name_product'),
            InlineKeyboardButton(text='Цена', callback_data='field_price')
        ],
        [
            InlineKeyboardButton(text='Описание', callback_data='field_description'),
            InlineKeyboardButton(text='Категория', callback_data='field_category')
        ]
    ]
)


def product_actions(product_id):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='✏️ Редактировать', callback_data=f'edit:{product_id}'),
                InlineKeyboardButton(text='🗑 Удалить', callback_data=f'delete:{product_id}')
            ]
        ]
    )


confirm_delete = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='✅ Да, удалить', callback_data='confirm_delete_yes'),
            InlineKeyboardButton(text='❌ Отмена', callback_data='confirm_delete_no')
        ]
    ]
)
