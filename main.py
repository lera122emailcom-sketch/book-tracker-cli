from models import Book
from storage import load_books, add_book, delete_book
from stats import calculate_average_rating, get_stats_by_author

def print_menu():
    print("\n" + "=" * 40)
    print("   ТРЕКЕР ПРОЧИТАННЫХ КНИГ")
    print("=" * 40)
    print("1. Добавить книгу")
    print("2. Показать все книги")
    print("3. Показать среднюю оценку")
    print("4. Статистика по авторам")
    print("5. Удалить книгу")
    print("6. Выход")
    print("=" * 40)

def input_book_data():
    author = input("Автор: ").strip()
    title = input("Название: ").strip()
    while True:
        try:
            rating = int(input("Оценка (1-5): "))
            if 1 <= rating <= 5:
                break
            print("Ошибка: введите число от 1 до 5")
        except ValueError:
            print("Ошибка: введите целое число")
    date_read = input("Дата прочтения (ГГГГ-ММ-ДД): ").strip()
    return Book(author=author, title=title, rating=rating, date_read=date_read)

def show_all_books():

