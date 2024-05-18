import sqlite3

conn = sqlite3.connect('db_name')
cursor = conn.cursor()

# Включаем поддержку внешних ключей
cursor.execute("PRAGMA foreign_keys = ON;")

# Создаем таблицу "postav" (поставщики)
cursor.execute('''
CREATE TABLE postav (
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   name VARCHAR(255) NOT NULL,
   address VARCHAR(255),
   phone VARCHAR(20),
   email VARCHAR(255)
);
''')

# Создаем таблицу "products" (товары)
cursor.execute('''
CREATE TABLE products (
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   Name VARCHAR(255) NOT NULL,
   Packing VARCHAR(255),
   Price DECIMAL(10, 2) NOT NULL,
   Quantity INT NOT NULL,
   ExpirationDate DATE NOT NULL,
   postav_id INT,
   FOREIGN KEY (postav_id) REFERENCES postav(id)
);
''')

# Создаем таблицу "suppilfarm" (товары от ФармЛенд)
cursor.execute('''
CREATE TABLE suppilfarm (
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   Name VARCHAR(255) NOT NULL,
   Packing VARCHAR(255),
   Price DECIMAL(10, 2) NOT NULL,
   Quantity INT NOT NULL,
   ExpirationDate DATE NOT NULL
);
''')

# Создаем таблицу "suppilbellec" (товары от БелЛекГроуп)
cursor.execute('''
CREATE TABLE suppilbellec (
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   Name VARCHAR(255) NOT NULL,
   Packing VARCHAR(255),
   Price DECIMAL(10, 2) NOT NULL,
   Quantity INT NOT NULL,
   ExpirationDate DATE NOT NULL
);
''')

# Создаем таблицу "suppillecfarm" (товары от Лекфарм)
cursor.execute('''
CREATE TABLE suppillecfarm (
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   Name VARCHAR(255) NOT NULL,
   Packing VARCHAR(255),
   Price DECIMAL(10, 2) NOT NULL,
   Quantity INT NOT NULL,
   ExpirationDate DATE NOT NULL
);
''')

# Добавляем данные в таблицу "postav"
cursor.execute("INSERT INTO postav (name, address, phone, email) VALUES ('ФармЛенд', 'ул. Ленина, 10', '+7 (495) 123-45-67', 'farmland@mail.ru')")
cursor.execute("INSERT INTO postav (name, address, phone, email) VALUES ('БелЛекГроуп', 'пр. Мира, 5', '+7 (812) 555-66-77', 'bellekgroup@mail.ru')")
cursor.execute("INSERT INTO postav (name, address, phone, email) VALUES ('Лекфарм', 'ул. Пушкина, 15', '+7 (343) 222-33-44', 'lekfarm@mail.ru')")

# Добавляем данные в таблицу "products"
cursor.execute("INSERT INTO products (Name, Packing, Price, Quantity, ExpirationDate, postav_id) VALUES ('Аспирин', '10 таблеток', 10.50, 100, '2024-03-15', 1)")
cursor.execute("INSERT INTO products (Name, Packing, Price, Quantity, ExpirationDate, postav_id) VALUES ('Парацетамол', '20 таблеток', 8.00, 150, '2024-04-20', 2)")
cursor.execute("INSERT INTO products (Name, Packing, Price, Quantity, ExpirationDate, postav_id) VALUES ('Анальгин', '10 таблеток', 7.50, 200, '2024-05-10', 3)")
cursor.execute("INSERT INTO products (Name, Packing, Price, Quantity, ExpirationDate, postav_id) VALUES ('Ибупрофен', '20 таблеток', 9.50, 120, '2024-06-05', 1)")
cursor.execute("INSERT INTO products (Name, Packing, Price, Quantity, ExpirationDate, postav_id) VALUES ('Цитрамон', '10 таблеток', 12.00, 180, '2024-07-15', 2)")
cursor.execute("INSERT INTO products (Name, Packing, Price, Quantity, ExpirationDate, postav_id) VALUES ('Но-шпа', '20 таблеток', 15.00, 100, '2024-08-20', 3)")
cursor.execute("INSERT INTO products (Name, Packing, Price, Quantity, ExpirationDate, postav_id) VALUES ('Амидопирин', '10 таблеток', 8.50, 160, '2024-09-10', 1)")
cursor.execute("INSERT INTO products (Name, Packing, Price, Quantity, ExpirationDate, postav_id) VALUES ('Панадол', '20 таблеток', 11.00, 140, '2024-10-05', 2)")
cursor.execute("INSERT INTO products (Name, Packing, Price, Quantity, ExpirationDate, postav_id) VALUES ('Темпалгин', '10 таблеток', 13.50, 130, '2024-11-15', 3)")
cursor.execute("INSERT INTO products (Name, Packing, Price, Quantity, ExpirationDate, postav_id) VALUES ('Нурофен', '20 таблеток', 14.00, 110, '2024-12-20', 1)")


cursor.execute("INSERT INTO suppilfarm (Name, Packing, Price, Quantity, ExpirationDate) VALUES ('Но-шпа', '20 таблеток', 15.00, 120, '2024-12-20')")
cursor.execute("INSERT INTO suppilfarm (Name, Packing, Price, Quantity, ExpirationDate) VALUES ('Аспирин', '10 таблеток', 10.50, 50, '2024-03-15')")
cursor.execute("INSERT INTO suppilfarm (Name, Packing, Price, Quantity, ExpirationDate) VALUES ('Ибупрофен', '20 таблеток', 9.50, 30, '2024-04-20')")
cursor.execute("INSERT INTO suppilfarm (Name, Packing, Price, Quantity, ExpirationDate) VALUES ('Амидопирин', '10 таблеток', 8.50, 40, '2024-05-10')")
cursor.execute("INSERT INTO suppilfarm (Name, Packing, Price, Quantity, ExpirationDate) VALUES ('Нурофен', '20 таблеток', 14.00, 60, '2024-06-05')")
cursor.execute("INSERT INTO suppilfarm (Name, Packing, Price, Quantity, ExpirationDate) VALUES ('Парацетамол', '10 таблеток', 8.00, 70, '2024-07-15')")
cursor.execute("INSERT INTO suppilfarm (Name, Packing, Price, Quantity, ExpirationDate) VALUES ('Цитрамон', '20 таблеток', 12.00, 80, '2024-08-20')")
cursor.execute("INSERT INTO suppilfarm (Name, Packing, Price, Quantity, ExpirationDate) VALUES ('Темпалгин', '10 таблеток', 13.50, 90, '2024-09-10')")
cursor.execute("INSERT INTO suppilfarm (Name, Packing, Price, Quantity, ExpirationDate) VALUES ('Панадол', '20 таблеток', 11.00, 100, '2024-10-05')")
cursor.execute("INSERT INTO suppilfarm (Name, Packing, Price, Quantity, ExpirationDate) VALUES ('Анальгин', '10 таблеток', 7.50, 110, '2024-11-15')")

# Добавляем данные в таблицу "suppilbellec"
cursor.execute("INSERT INTO suppilbellec (Name, Packing, Price, Quantity, ExpirationDate) VALUES ('Парацетамол', '10 таблеток', 8.00, 70, '2024-05-10')")
cursor.execute("INSERT INTO suppilbellec (Name, Packing, Price, Quantity, ExpirationDate) VALUES ('Ибупрофен', '20 таблеток', 9.50, 40, '2024-06-05')")
cursor.execute("INSERT INTO suppilbellec (Name, Packing, Price, Quantity, ExpirationDate) VALUES ('Аспирин', '10 таблеток', 10.50, 50, '2024-03-15')")
cursor.execute("INSERT INTO suppilbellec (Name, Packing, Price, Quantity, ExpirationDate) VALUES ('Цитрамон', '20 таблеток', 12.00, 30, '2024-04-20')")
cursor.execute("INSERT INTO suppilbellec (Name, Packing, Price, Quantity, ExpirationDate) VALUES ('Но-шпа', '10 таблеток', 15.00, 60, '2024-07-15')")
cursor.execute("INSERT INTO suppilbellec (Name, Packing, Price, Quantity, ExpirationDate) VALUES ('Амидопирин', '20 таблеток', 8.50, 80, '2024-08-20')")
cursor.execute("INSERT INTO suppilbellec (Name, Packing, Price, Quantity, ExpirationDate) VALUES ('Темпалгин', '10 таблеток', 13.50, 90, '2024-09-10')")
cursor.execute("INSERT INTO suppilbellec (Name, Packing, Price, Quantity, ExpirationDate) VALUES ('Панадол', '20 таблеток', 11.00, 100, '2024-10-05')")
cursor.execute("INSERT INTO suppilbellec (Name, Packing, Price, Quantity, ExpirationDate) VALUES ('Анальгин', '10 таблеток', 7.50, 110, '2024-11-15')")
cursor.execute("INSERT INTO suppilbellec (Name, Packing, Price, Quantity, ExpirationDate) VALUES ('Нурофен', '20 таблеток', 14.00, 120, '2024-12-20')")

# Добавляем данные в таблицу "suppillecfarm"
cursor.execute("INSERT INTO suppillecfarm (Name, Packing, Price, Quantity, ExpirationDate) VALUES ('Анальгин', '10 таблеток', 7.50, 60, '2024-07-15')")
cursor.execute("INSERT INTO suppillecfarm (Name, Packing, Price, Quantity, ExpirationDate) VALUES ('Но-шпа', '20 таблеток', 15.00, 80, '2024-08-20')")
cursor.execute("INSERT INTO suppillecfarm (Name, Packing, Price, Quantity, ExpirationDate) VALUES ('Аспирин', '10 таблеток', 10.50, 90, '2024-09-10')")
cursor.execute("INSERT INTO suppillecfarm (Name, Packing, Price, Quantity, ExpirationDate) VALUES ('Парацетамол', '20 таблеток', 8.00, 100, '2024-10-05')")
cursor.execute("INSERT INTO suppillecfarm (Name, Packing, Price, Quantity, ExpirationDate) VALUES ('Ибупрофен', '10 таблеток', 9.50, 110, '2024-11-15')")
cursor.execute("INSERT INTO suppillecfarm (Name, Packing, Price, Quantity, ExpirationDate) VALUES ('Цитрамон', '20 таблеток', 12.00, 120, '2024-12-20')")
cursor.execute("INSERT INTO suppillecfarm (Name, Packing, Price, Quantity, ExpirationDate) VALUES ('Темпалгин', '10 таблеток', 13.50, 50, '2024-03-15')")
cursor.execute("INSERT INTO suppillecfarm (Name, Packing, Price, Quantity, ExpirationDate) VALUES ('Панадол', '20 таблеток', 11.00, 30, '2024-04-20')")
cursor.execute("INSERT INTO suppillecfarm (Name, Packing, Price, Quantity, ExpirationDate) VALUES ('Амидопирин', '10 таблеток', 8.50, 40, '2024-05-10')")
cursor.execute("INSERT INTO suppillecfarm (Name, Packing, Price, Quantity, ExpirationDate) VALUES ('Нурофен', '20 таблеток', 14.00, 60, '2024-06-05')")

conn.commit()
conn.close()












# db=sqlite3.connect('apteka.db')
# cors = db.cursor()


# cors.execute('''
# CREATE TABLE  IF NOT EXISTS postav (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name VARCHAR(255) NOT NULL,
#     address VARCHAR(255),
#     phone VARCHAR(20),
#     email VARCHAR(255)
# );

# CREATE TABLE suppilfarmlend (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     Name VARCHAR(255) NOT NULL,
#     Packing VARCHAR(255),
#     Price DECIMAL(10, 2) NOT NULL,
#     Supplier VARCHAR(255) NOT NULL,
#     Quantity INT NOT NULL,
#     ExpirationDate DATE NOT NULL,
#     postav_id INT,
#     FOREIGN KEY (postav_id) REFERENCES postav(id)
# );
# ''')


# cors.execute('''
#  CREATE TABLE products (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     Name VARCHAR(255) NOT NULL,
#     Packing Array VARCHAR(255),
#     Price DECIMAL(10, 2) NOT NULL,
#     Supplier VARCHAR(255) NOT NULL,
#     Quantity INT NOT NULL,
#     Expiration Date DATE NOT NULL
#  )
# ''')

# cors.execute("INSERT INTO products VALUES (null,'Аспирин', '20 таблеток', 10.50, 'Фармацевтическая компания А', 100, '2024-06-15')")
# cors.execute("INSERT INTO products VALUES (null,'Парацетамол', '20 таблеток', 8.75, 'Фармацевтическая компания Б', 150, '2024-08-20')")
# cors.execute("INSERT INTO products VALUES (null,'Ибупрофен', '10 таблеток', 9.25, 'Фармацевтическая компания В', 80, '2024-07-10')")
# cors.execute("INSERT INTO products VALUES (null,'Цитрамон', '10 таблеток', 11.00, 'Фармацевтическая компания А', 120, '2024-09-05')")
# cors.execute("INSERT INTO products VALUES (null,'Анальгин', ' 20 таблеток', 7.50, 'Фармацевтическая компания А', 90, '2024-06-25')")
# cors.execute("INSERT INTO products VALUES (null,'Амоксициллин', '10 таблеток', 15.00, 'Фармацевтическая компания Б', 75, '2024-08-10')")
# cors.execute("INSERT INTO products VALUES (null,'Цефтриаксон', '2 г', 25.00, 'Фармацевтическая компания В', 60, '2024-07-20')")
# cors.execute("INSERT INTO products VALUES (null,'Диклофенак', '20 таблеток', 12.00, 'Фармацевтическая компания В', 110, '2024-09-15')")
# cors.execute("INSERT INTO products VALUES (null,'Нимесулид', '100 мг', 18.50, 'Фармацевтическая компания И', 50, '2024-06-30')")
# cors.execute("INSERT INTO products VALUES (null,'Флуконазол', '300 мг', 17.75, 'Фармацевтическая компания К', 40, '2024-08-15')")

# cors.execute("INSERT INTO products VALUES (null,'Аспирин', '10 таблеток', 12.50, 'Фармацевтическая компания А', 100, '2024-06-15')")
# cors.execute("INSERT INTO products VALUES (null,'Парацетамол', '30 таблеток', 7.75, 'Фармацевтическая компания Б', 150, '2024-08-20')")
# cors.execute("INSERT INTO products VALUES (null,'Ибупрофен', '30 таблеток', 3.25, 'Фармацевтическая компания В', 80, '2024-07-10')")
# cors.execute("INSERT INTO products VALUES (null,'Цитрамон', '30 таблеток', 13.00, 'Фармацевтическая компания А', 120, '2024-09-05')")
# cors.execute("INSERT INTO products VALUES (null,'Анальгин', ' 10 таблеток', 33.50, 'Фармацевтическая компания А', 90, '2024-06-25')")
# cors.execute("INSERT INTO products VALUES (null,'Амоксициллин', '20 таблеток', 12.00, 'Фармацевтическая компания Б', 75, '2024-08-10')")
# cors.execute("INSERT INTO products VALUES (null,'Цефтриаксон', '12 г', 22.00, 'Фармацевтическая компания В', 60, '2024-07-20')")
# cors.execute("INSERT INTO products VALUES (null,'Диклофенак', '120 таблеток', 12.00, 'Фармацевтическая компания В', 110, '2024-09-15')")
# cors.execute("INSERT INTO products VALUES (null,'Нимесулид', '200 мг', 12.50, 'Фармацевтическая компания И', 50, '2024-06-30')")
# cors.execute("INSERT INTO products VALUES (null,'Флуконазол', '200 мг', 12.75, 'Фармацевтическая компания К', 40, '2024-08-15')")



# print(cors.fetchall())
# db.commit()
# db.close()