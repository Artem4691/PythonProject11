create_product_table = """
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name_product TEXT,
        price INTEGER,
        product_id INTEGER NOT NULL
    )
"""

create_products_detail_table = """
    CREATE TABLE IF NOT EXISTS products_detail (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT,
        photo TEXT,
        category TEXT,
        product_id INTEGER NOT NULL
    )
"""

create_table_staff = """
    CREATE TABLE IF NOT EXISTS staff (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        full_name TEXT
    )
"""

create_movies_table = """
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        genre TEXT NOT NULL,
        film_id INTEGER NOT NULL
    )
"""

create_movies_detail_table = """
    CREATE TABLE IF NOT EXISTS movies_detail (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        rating INTEGER NOT NULL,
        description TEXT NOT NULL,
        film_id INTEGER NOT NULL
    )
"""

add_product = 'INSERT INTO products (name_product, price, product_id) VALUES (?, ?, ?)'
add_product_detail = 'INSERT INTO products_detail (description, photo, category, product_id) VALUES (?, ?, ?, ?)'

get_products = """
SELECT p.name_product, p.price, pd.photo, pd.description, pd.category, p.product_id
FROM products p
INNER JOIN products_detail pd ON p.product_id = pd.product_id;
"""

delete_product = 'DELETE FROM products WHERE product_id = ?'
delete_product_detail = 'DELETE FROM products_detail WHERE product_id = ?'

check_staff = 'SELECT user_id FROM staff WHERE user_id = ?'
insert_staff = 'INSERT INTO staff (user_id, full_name) VALUES (?, ?)'
get_staff_list = 'SELECT user_id, full_name FROM staff'

add_movie = 'INSERT INTO movies (title, genre, film_id) VALUES (?, ?, ?)'
add_movie_detail = 'INSERT INTO movies_detail (rating, description, film_id) VALUES (?, ?, ?)'

get_movies = """
SELECT m.title, m.genre, md.rating, md.description, m.film_id
FROM movies m
INNER JOIN movies_detail md ON m.film_id = md.film_id;
"""



def update_product():
    return None


def delete_product():
    return None


def delete_product_detail():
    return None