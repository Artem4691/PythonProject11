import aiosqlite
from database import queries

path_db = 'database/bot.db'


async def init_db():
    async with aiosqlite.connect(path_db) as conn:
        await conn.execute(queries.create_product_table)
        await conn.execute(queries.create_products_detail_table)
        await conn.execute(queries.create_table_staff)
        await conn.execute(queries.create_movies_table)
        await conn.execute(queries.create_movies_detail_table)
        await conn.commit()
    print('DB connected!')


async def add_product_db(name, price, description, photo, category, product_id):
    async with aiosqlite.connect(path_db) as conn:
        await conn.execute(queries.add_product, (name, price, product_id))
        await conn.execute(queries.add_product_detail, (description, photo, category, product_id))
        await conn.commit()


async def get_products_db():
    async with aiosqlite.connect(path_db) as conn:
        cursor = await conn.execute(queries.get_products)
        products = await cursor.fetchall()
        return products


async def update_product_db(field, value, product_id):
    async with aiosqlite.connect(path_db) as conn:
        if field in ('name_product', 'price'):
            query = f"UPDATE products SET {field} = ? WHERE product_id = ?"
        else:
            query = f"UPDATE products_detail SET {field} = ? WHERE product_id = ?"
        await conn.execute(query, (value, product_id))
        await conn.commit()


async def delete_product_db(product_id):
    async with aiosqlite.connect(path_db) as conn:
        await conn.execute(queries.delete_product, (product_id,))
        await conn.execute(queries.delete_product_detail, (product_id,))
        await conn.commit()


async def is_staff_db(user_id: int):
    async with aiosqlite.connect(path_db) as conn:
        cursor = await conn.execute(queries.check_staff, (user_id,))
        row = await cursor.fetchone()
        return row is not None


async def add_staff_db(user_id, full_name):
    async with aiosqlite.connect(path_db) as conn:
        await conn.execute(queries.insert_staff, (user_id, full_name))
        await conn.commit()


async def get_staff_list_db():
    async with aiosqlite.connect(path_db) as conn:
        cursor = await conn.execute(queries.get_staff_list)
        staff_list = await cursor.fetchall()
        return staff_list


async def add_movie_db(title, genre, film_id):
    async with aiosqlite.connect(path_db) as conn:
        await conn.execute(queries.add_movie, (title, genre, film_id))
        await conn.commit()


async def add_movie_detail_db(rating, description, film_id):
    async with aiosqlite.connect(path_db) as conn:
        await conn.execute(queries.add_movie_detail, (rating, description, film_id))
        await conn.commit()


async def get_movies_db():
    async with aiosqlite.connect(path_db) as conn:
        cursor = await conn.execute(queries.get_movies)
        movies = await cursor.fetchall()
        return movies
