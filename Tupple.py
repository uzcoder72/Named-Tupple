import requests
import psycopg2

url = 'https://dummyjson.com/products/'

r = requests.get(url)

conn = psycopg2.connect(dbname='n47',
                        user='postgres',
                        password='123',
                        host='localhost',
                        port=5432)

create_table_products_query = """
    CREATE TABLE IF NOT EXISTS products (
        id SERIAL PRIMARY KEY,
        title VARCHAR(255),
        description TEXT,
        price INT,
        discountPercentage FLOAT,
        rating FLOAT,
        stock INT,
        brand VARCHAR(255),
        category VARCHAR(200),
        thumbnail VARCHAR(255),
        images TEXT
    );
"""

cur = conn.cursor()
cur.execute(create_table_products_query)
conn.commit()

insert_into_query = """
    INSERT INTO products (title, description, price, discountPercentage, rating, stock, brand, category, thumbnail, images)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
"""

for product in r.json()['products']:
    cur.execute(insert_into_query, (
        product['title'], product['description'], product['price'], product['discountPercentage'],
        product['rating'], product['stock'], product['brand'], product['category'],
        product['thumbnail'], str(product['images'])
    ))
    conn.commit()

print("Data inserted successfully!")
