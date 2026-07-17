import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.library import Library

def print_books(books):
    """Красиво выводит списое книг"""
    
    if not books:
        print("Книг не найдено")
        return
    
    print(f"\nНайдено книг: {len(books)}")
    print("=" * 70)
    for book in books:
        print(book)
    print("="*70)

def print_stats(stats):
    """Выводит статистику"""

    print(f"""\n📊 СТАТИСТИКА БИБЛИОТЕКИ"
    "=" * 40
    📚 Всего книг: {stats['total']}
    🗃 В наличии: {stats['available']}
    📝 Выдано: {stats['borrowed']}
    "-"*40""")

def main():
    library = Library()

    while True:
        print(""""\n"+ 40
              🏛 БИБЛИОТЕКА КНИГ
              1️⃣ Добавить книгу
              2️⃣ Удалить книгу
              3️⃣ Найти книгу
              4️⃣ Показать все книги
              5️⃣ Изменить статус книги
              6️ Показать статистику
              7️ выход
            """)
        choice = input("Решение за вами:")

        if choice == "1":
            title = input("Название действие: ")
            author = input("Автор: ")
            try:
                year = int(input("Год: "))
                library.add_book(title, author, year)
            except ValueError:
                print("Введите число!")
            
        elif choice == "2":
            books = library.get_all_books()
            if not books:
                print("Библиотека пуста")
                continue
            print_books(books)
            
            try:
                book_id = int(input("ID книги для удаления: "))
                library.delete_book(book_id)
            except ValueError:
                print("Введите число!")
        elif choice == '3':
            query = input("Введите название, автора или год: ")
            results = library.find_books(query)
            print_books(results)

        elif choice == '4':
            books = library.get_all_books()
            print_books(books)

        elif choice == '5':
            books = library.get_all_books()
            if not books:
                print("Библиотека пуста")
                continue
            print_books(books)

            try:
                book_id = int(input("ID книги: "))
                print("Доступные статусы: 'в наличии', 'выдана'")
                new_status = input("Новый статус: ").strip().lower()
                library.update_status(book_id, new_status)
            except ValueError:
                print("Введите число!")

        elif choice == '6':
            stats = library.get_stats()
            print_stats(stats)

        elif choice == '7':
            print("До встречи!")
            break

        else:
            print("Неверный выбор")

if __name__ == "__main__":
    main()