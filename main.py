import logging
import asyncio
from aiogram.types import BotCommand
from config import bot, dp
from handlers import commands, echo, hw2, fsm, fsm_add_product, fsm_edit_product, fsm_staff_registration, fsm_delete_product
from database import db


async def set_commands():
    bot_commands = [
        BotCommand(command='start', description='Старт бота'),
        BotCommand(command='mem', description='отправка мема'),
        BotCommand(command='add_product', description='Добавление товара'),
        BotCommand(command='products', description='Получение товаров')
    ]
    await bot.set_my_commands(bot_commands)


async def on_startup():
    await db.init_db()
    await set_commands()
    await bot.send_message(chat_id=7841711547, text="Бот включен!")


dp.include_router(router=commands.router_commands)
dp.include_router(router=hw2.router_hw2)
dp.include_router(router=fsm.router_fsm)
dp.include_router(router=fsm_add_product.router_add_product)
dp.include_router(router=fsm_edit_product.router_edit_product)
dp.include_router(router=fsm_staff_registration.router_staff)
dp.include_router(router=fsm_delete_product.router_delete_product)
dp.include_router(router=echo.router_echo)

dp.startup.register(on_startup)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(dp.start_polling(bot))



