from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from database.db import add_movie_db, add_movie_detail_db, get_movies_db

router_fsm = Router()


class MovieForm(StatesGroup):
    title = State()
    genre = State()
    rating = State()
    description = State()
    film_id = State()


@router_fsm.message(Command("form"))
async def start_form(message: Message, state: FSMContext):
    await state.set_state(MovieForm.title)
    await message.answer("Давай добавим фильм в базу! 🎬\n\nШаг 1/5. Введите название фильма:")


@router_fsm.message(MovieForm.title)
async def process_title(message: Message, state: FSMContext):
    await state.update_data(title=message.text)
    await state.set_state(MovieForm.genre)
    await message.answer("Шаг 2/5. Укажите жанр фильма:")


@router_fsm.message(MovieForm.genre)
async def process_genre(message: Message, state: FSMContext):
    await state.update_data(genre=message.text)
    await state.set_state(MovieForm.rating)
    await message.answer("Шаг 3/5. Поставьте фильму оценку от 1 до 10:")


@router_fsm.message(MovieForm.rating)
async def process_rating(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Ошибка! Оценка должна быть числом. Введите цифру от 1 до 10:")
        return

    rating = int(message.text)
    if rating < 1 or rating > 10:
        await message.answer("Оценка должна быть в пределах от 1 до 10. Попробуйте еще раз:")
        return

    await state.update_data(rating=rating)
    await state.set_state(MovieForm.description)
    await message.answer("Шаг 4/5. Напишите короткий отзыв или описание фильма:")


@router_fsm.message(MovieForm.description)
async def process_description(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    await state.set_state(MovieForm.film_id)
    await message.answer("Шаг 5/5. Введите уникальный номер (ID) фильма (например, 101):")


@router_fsm.message(MovieForm.film_id)
async def process_film_id(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Ошибка! ID фильма должен быть числом. Попробуйте еще раз:")
        return

    film_id = int(message.text)
    await state.update_data(film_id=film_id)
    data = await state.get_data()


    await add_movie_db(
        title=data['title'],
        genre=data['genre'],
        film_id=data['film_id']
    )
    await add_movie_detail_db(
        rating=data['rating'],
        description=data['description'],
        film_id=data['film_id']
    )

    result_text = (
        "✅ **Фильм успешно сохранён в две таблицы!**\n\n"
        f"🆔 **ID:** {data['film_id']}\n"
        f"🎬 **Название:** {data['title']}\n"
        f"🎭 **Жанр:** {data['genre']}\n"
        f"⭐ **Оценка:** {data['rating']}/10\n"
        f"📝 **Описание:** {data['description']}"
    )

    await message.answer(result_text, parse_mode="Markdown")
    await state.clear()


@router_fsm.message(Command("movies"))
async def show_movies(message: Message):
    movies = await get_movies_db()

    if not movies:
        await message.answer("Список фильмов пока пуст. Добавьте первый через /form!")
        return

    for title, genre, rating, description, film_id in movies:
        text = (
            f"🎬 **{title}** (ID: {film_id})\n"
            f"🎭 **Жанр:** {genre}\n"
            f"⭐ **Оценка:** {rating}/10\n"
            f"📝 **Описание:** {description}"
        )
        await message.answer(text, parse_mode="Markdown")
