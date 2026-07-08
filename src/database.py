import sqlite3
import os

DB_PATH = "data/library.db"

def get_connection():
    """
    Создает и возвращает подключение к базе данных SQLite.
    Создаёт папку data, при её отсутствии.
    """

    #create folder "data" if It isn't
    os.makedirs("data", exist_ok = True)

    return sqlite3.connect(DB_PATH)

def init_database():
    """
    Create table "bools", if it isn't.
    This function open once at startup programm.
    """

    #get connection
    conn = get_connection()

    #Create cursor - the tool for make reqests
    cursor = conn.cursor()

    #SQL - reqest for create table
    cursor.execute("""
        CREATE TABLE IF NOT EXIST books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year INTEGER NOT NULL,
            status TEXT DEFAULT 'в наличии'
        )
""")
    
    #save changes
    conn.commit()

    #close connection
    conn.close()

    print("База данных инициализирована")

