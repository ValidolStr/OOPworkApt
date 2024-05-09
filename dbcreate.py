import sqlite3

db=sqlite3.connect('apteka.db')
cors = db.cursor()
#cors.execute("""
 #           CREATE TABLE USERS (
  #            login text,
  #              password text)            
   #          """)
cors.execute("INSERT INTO users VALUES ('12', '12')")
cors.execute(" SELECT * FROM users  ")
print(cors.fetchall())
db.commit()
db.close()