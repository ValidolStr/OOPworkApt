import sqlite3

db=sqlite3.connect('apteka.db')
cors = db.cursor()

cors.execute('''
 CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name VARCHAR(255) NOT NULL,
    Packing Array VARCHAR(255),
    Price DECIMAL(10, 2) NOT NULL,
    Supplier VARCHAR(255) NOT NULL,
    Quantity INT NOT NULL,
    Expiration Date DATE NOT NULL
 )
''')

cors.execute("INSERT INTO products VALUES (null,'Аспирин', '20 таблеток', 10.50, 'Фармацевтическая компания А', 100, '2024-06-15')")
cors.execute("INSERT INTO products VALUES (null,'Парацетамол', '20 таблеток', 8.75, 'Фармацевтическая компания Б', 150, '2024-08-20')")
cors.execute("INSERT INTO products VALUES (null,'Ибупрофен', '10 таблеток', 9.25, 'Фармацевтическая компания В', 80, '2024-07-10')")
cors.execute("INSERT INTO products VALUES (null,'Цитрамон', '10 таблеток', 11.00, 'Фармацевтическая компания А', 120, '2024-09-05')")
cors.execute("INSERT INTO products VALUES (null,'Анальгин', ' 20 таблеток', 7.50, 'Фармацевтическая компания А', 90, '2024-06-25')")
cors.execute("INSERT INTO products VALUES (null,'Амоксициллин', '10 таблеток', 15.00, 'Фармацевтическая компания Б', 75, '2024-08-10')")
cors.execute("INSERT INTO products VALUES (null,'Цефтриаксон', '2 г', 25.00, 'Фармацевтическая компания В', 60, '2024-07-20')")
cors.execute("INSERT INTO products VALUES (null,'Диклофенак', '20 таблеток', 12.00, 'Фармацевтическая компания В', 110, '2024-09-15')")
cors.execute("INSERT INTO products VALUES (null,'Нимесулид', '100 мг', 18.50, 'Фармацевтическая компания И', 50, '2024-06-30')")
cors.execute("INSERT INTO products VALUES (null,'Флуконазол', '300 мг', 17.75, 'Фармацевтическая компания К', 40, '2024-08-15')")

cors.execute("INSERT INTO products VALUES (null,'Аспирин', '10 таблеток', 12.50, 'Фармацевтическая компания А', 100, '2024-06-15')")
cors.execute("INSERT INTO products VALUES (null,'Парацетамол', '30 таблеток', 7.75, 'Фармацевтическая компания Б', 150, '2024-08-20')")
cors.execute("INSERT INTO products VALUES (null,'Ибупрофен', '30 таблеток', 3.25, 'Фармацевтическая компания В', 80, '2024-07-10')")
cors.execute("INSERT INTO products VALUES (null,'Цитрамон', '30 таблеток', 13.00, 'Фармацевтическая компания А', 120, '2024-09-05')")
cors.execute("INSERT INTO products VALUES (null,'Анальгин', ' 10 таблеток', 33.50, 'Фармацевтическая компания А', 90, '2024-06-25')")
cors.execute("INSERT INTO products VALUES (null,'Амоксициллин', '20 таблеток', 12.00, 'Фармацевтическая компания Б', 75, '2024-08-10')")
cors.execute("INSERT INTO products VALUES (null,'Цефтриаксон', '12 г', 22.00, 'Фармацевтическая компания В', 60, '2024-07-20')")
cors.execute("INSERT INTO products VALUES (null,'Диклофенак', '120 таблеток', 12.00, 'Фармацевтическая компания В', 110, '2024-09-15')")
cors.execute("INSERT INTO products VALUES (null,'Нимесулид', '200 мг', 12.50, 'Фармацевтическая компания И', 50, '2024-06-30')")
cors.execute("INSERT INTO products VALUES (null,'Флуконазол', '200 мг', 12.75, 'Фармацевтическая компания К', 40, '2024-08-15')")



print(cors.fetchall())
db.commit()
db.close()