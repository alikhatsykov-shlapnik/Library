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

    print("\n📊 СТАТИСТИКА БИБЛИОТЕКИ")
    print("=" * 40)
    print(f"📚 Всего книг: {stats['total']}")
    print(f"🗃 В наличии: {stats['available']}")
    print(f"📝 Выдано: {stats['borrowed']}")
    print("-"*40)

def main():
    try:
        library = Library()
    except Exception as e:
        print(f"Ошибка при создании библиотеки: {e}")

    while True:
        try:
            print("\n"+"="*40)
            print("🏛 БИБЛИОТЕКА КНИГ")
            print("1️⃣ Добавить книгу")
            print("2️⃣ Удалить книгу")
            print("3️⃣ Найти книгу")
            print("4️⃣ Показать все книги")
            print("5️⃣ Изменить статус книги")
            print("6️ Показать статистику")
            print("7️ выход")

            choice = input("Решение за вами:")

            if choice == "1":
                title = input("Название: ")
                author = input("Автор: ")
                try:
                    year = int(input("Год: "))
                    library.add_book(title, author, year)
                except ValueError:
                    print("Введите число!")
                
            elif choice == "2":
                try:
                    books = library.get_all_books()
                    if not books:
                        print("Библиотека пуста")
                        continue
                    print_books(books)
                    book_id = int(input("ID книги для удаления: "))
                    library.delete_book(book_id)
                except ValueError:
                    for book in books:
                        print(dir(book))
                    print("Введите число!")
                except Exception as e:
                    for book in books:
                        print(dir(book))

                    print(f"Ошибка при удалении: {e}")
                    
            elif choice == '3':
                try:
                    query = input("Введите название, автора или год: ")
                    results = library.find_books(query)
                    print_books(results)
                except Exception as e:
                    print(f"Ошибка при поиске: {e}")

            elif choice == '4':
                try:
                    books = library.get_all_books()
                    print_books(books)
                except Exception as e:
                    print(f"Ошибка при получении книг: {e}")

            elif choice == '5':
                try:
                    books = library.get_all_books()
                    if not books:
                        print("Библиотека пуста")
                        continue
                    print_books(books)

                    book_id = int(input("ID книги: "))
                    print("Доступные статусы: 'в наличии', 'выдана'")
                    new_status = input("Новый статус: ").strip().lower()
                    library.update_status(book_id, new_status)
                except ValueError:
                    print("Введите число!")
                except Exception as e:
                    print(f"Ошибка при изменении статуса: {e}")

            elif choice == '6':
                try:
                    stats = library.get_stats()
                    print_stats(stats)
                except Exception as e:
                    print(f"Ошибка при получении статистики: {e}")

            elif choice == '7':
                print("До встречи!")
                break

            else:
                print("Неверный выбор")
        except KeyboardInterrupt:
            print("До встречи!")
            break
        except Exception as e:
            print(f"Непредвиденная ошибка: {e}")

if __name__ == "__main__":
    main()