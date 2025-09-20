import sqlite3


def create_table_delivery():
  connection = sqlite3.connect("mft_db.db")
  cursor = connection.cursor()
  cursor.execute("create table delivery(id integer primary key autoincrement, product text, oder_datetime text, status text, deliver_datetime text)")
  connection.commit()
  connection.close()



def save_delivery(product, oder_datetime, status, deliver_datetime):
    connection = sqlite3.connect("mft_db.db")
    cursor = connection.cursor()
    cursor.execute("insert into delivery(product, oder_datetime, status, deliver_datetime) values (?, ?, ?, ?)",
                   [product, oder_datetime, status, deliver_datetime])
    connection.commit()
    connection.close()
