import sqlite3

conn = sqlite3.connect('mi_base_de_datos.db')

cursor = conn.cursor()
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS PERSONA (
      CUIL INTEGER PRIMARY KEY,
      NOMBRE TEXT NOT NULL,
      CALLE TEXT,
      NUMERO INTEGER,
      COMUNA TEXT,
      CIUDAD TEXT
);''')
			   
conn.commit()
conn.close()