import sqlite3
import logging

conn = sqlite3.connect('store.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY,name TEXT NOT NULL,price REAL NOT NULL)
''')
conn.commit()

def add_product(name, price):
    cursor.execute('INSERT INTO products (name, price) VALUES (?, ?)', (name, price))
    conn.commit()
    print('+1.')

def delete_product(product_id):
    cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
    conn.commit()
    print('обмін з рус успішний.')


def edit_product(product_id, new_name, new_price):
    cursor.execute('UPDATE products SET name = ?, price = ? WHERE id = ?', (new_name, new_price, product_id))
    conn.commit()
    print('ну все капець.')

def view_products():
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    print('Полонені:')
    for product in products:
        print(f'ID: {product[0]}, Назва: {product[1]}, Ціна: {product[2]}')


print('Слава Україні!')
print(input("password: "))


while True:
    print('\nМеню:')
    print('1. Шо в мене є?')
    print('2. +1 орк')
    print('3. на москву!')
    print('4. кастрація')
    print('5. тікай з міста')

    choice = input('вибирай спецоперацію: ')

    if choice == '1':
        view_products()
    elif choice == '2':
        name = input(': ')
        price = float(input('Введіть ціну орка: '))
        add_product(name, price)
    elif choice == '3':
        product_id = input('Введіть ID орка, якого потрібно знищити: ')
        delete_product(product_id)
    elif choice == '4':
        product_id = input('Введіть ID орка, який потрібно кастрирувати: ')
        new_name = input('Введіть нову назву орка: ')
        new_price = float(input('Введіть нову ціну орка: '))
        edit_product(product_id, new_name, new_price)
    elif choice == '5':
        print('БаНдЕрА!')
        break
    else:
        print('еееееее ти шо не наш?????.')

cursor.close()
conn.close()