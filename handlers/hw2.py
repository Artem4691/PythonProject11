from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
import random
from datetime import datetime

router_hw2 = Router()

JOKES = [
    "Программист ставит рядом с кроватью два стакана: один с водой — на случай, если захочется пить, а второй пустой — на случай, если не захочется.",
    "— Доктор, я постоянно разговариваю сам с собой.\n— Ничего страшного, главное — не спорьте!",
    "Кот — это жидкость, которая принимает форму любого свободного места на клавиатуре.",
    "Оптимист видит стакан наполовину полным. Пессимист — наполовину пустым. Программист видит, что стакан в два раза больше, чем нужно.",
    "Вчера лег спать пораньше — в два часа ночи. Сегодня."
]

@router_hw2.message(Command("time"))
async def cmd_time(message: Message):
    now = datetime.now().strftime("%d.%m.%Y %H:%M")
    await message.answer(f"Сейчас: {now}")

@router_hw2.message(Command("random"))
async def cmd_random(message: Message):
    number = random.randint(1, 100)
    await message.answer(f"Твоё случайное число: {number}")

@router_hw2.message(Command("joke"))
async def cmd_joke(message: Message):
    joke = random.choice(JOKES)
    await message.answer(joke)

