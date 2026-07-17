from database import get_connection, init_database
from book import Book

class Library:

    def __init__(self):
        """Инициализация библиотеки: создание БД при запуске."""
        init_database()

    def add_book(self, title, author, year):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO books (title, author, year) VALUES (?, ?, ?)",
            (title, author, year)
        )
        conn.commit()

        book_id = cursor.lastrowid
        conn.close()

        book = Book(title, author, year, book_id)
        print(f"Книга '{title}' добавлена! (ID: {book_id})")
        return book
    
    def get_all_books(self):
        """Список всех книг"""
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id, title, author, year, status FROM books ORDER BY id")
        rows = cursor.fetchall()
        conn.close()

        books = []
        for row in rows:
            book = Book(
                title=row[1],
                author=row[2],
                year=row[3],
                book_id=row[0],
                status=row[4]
            )
            books.append(book)
            return books
        def find_books(self, query):
            """поиск книги по названию, автору или году(частичное совпадение)"""
            conn = get_connection()
            cursor = conn.cursor()
            
            cursor.execute("""
                SELECT id, title, author, year, status
                FROM books
                WHERE title LIKE? OR author LIKE? OR year LIKE?
                ORDER BY id
            """, (f"%{query}%", f"%{query}%", f"%{query}%"))

            rows = cursor.fetchall()
            conn.close()

            books = []
            for row in rows:
                book = Book(
                    title=row[1],
                    author=row[2],
                    year=row[3],
                    book_id=row[0],
                    status=row[4]
                )
                books.append(book)
            return books
        def delete_book(self, book_id):
            """Удаляет книгу по ID"""
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
            conn.commit()

            deleted = cursor.rowcount > 0
            conn.close()

            if deleted:
                print(f"Книга с ID {book_id} удалена")
            else:
                print(f"Книга с ID {book_id} не найдена")

            return deleted
        
        def update_status(self, book_id, new_status):
            if new_status not in ["в наличии", "выдана"]:
                print("Неверный статус. Используйте 'в наличии' или 'выдана'")
                return False
            
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE books SET status = ? WHERE id = ?",
                (new_status, book_id)
            )
            conn.commit()

            updated = cursor.rowcount > 0
            conn.close()

            print(f"Статус книги ID {book_id} изменен на '{new_status}'" if updated else f"Книга с ID {book_id} не найдена")

            return updated
        
        def get_stats(self):
            """Возвращает статистику библиотеки"""
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT COUNT(*) FROM books")
            total = cursor.fetchone()[0]

            cursor.execute("SELECT COUNT(*) FROM books WHERE status = 'в наличии'")
            available = cursor.fetchone()[0]

            cursor.execute("SELECT COUNT(*) FROM books WHERE status = 'выдана'")
            borrowed = cursor.fetchone()[0]

            conn.close()

            return {
                "total": total,
                "available": available,
                "borrowed": borrowed
            }