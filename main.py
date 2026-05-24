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
    books = load_books()
    if not books:
        print("\nСписок книг пуст.")
        return
    print("\n--- Все книги ---")
    for i, book in enumerate(books, 1):
        print(f"{i}. {book.author} — «{book.title}» | Оценка: {book.rating}/5 | Дата: {book.date_read}")

def show_average_rating():
    books = load_books()
    avg = calculate_average_rating(books)
    print(f"\nСредняя оценка: {avg}/5 (всего книг: {len(books)})")

def show_author_stats():
    books = load_books()
    stats = get_stats_by_author(books)
    if not stats:
        print("\nНет данных для статистики.")
        return
    print("\n--- Статистика по авторам ---")
    for author, data in stats.items():
        print(f"{author}: {data['count']} кн., средняя оценка: {data['avg_rating']}/5")

def delete_book_action():
    author = input("Автор книги для удаления: ").strip()
    title = input("Название книги для удаления: ").strip()
    if delete_book(author, title):
        print(f"\nКнига «{title}» удалена.")
    else:
        print(f"\nКнига не найдена.")

def main():
    while True:
        print_menu()
        choice = input("\nВыберите действие (1-6): ").strip()

        if choice == "1":
            try:
                book = input_book_data()
                if add_book(book):
                    print(f"\nКнига «{book.title}» добавлена!")
                else:
                    print("\nТакая книга уже есть в трекере.")
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == "2":
            show_all_books()

        elif choice == "3":
            show_average_rating()

        elif choice == "4":
            show_author_stats()

        elif choice == "5":
            delete_book_action()

        elif choice == "6":
            print("\nВыход из программы.")
            break

        else:
            print("\nНеверный выбор. Попробуйте снова.")

        input("\nНажмите Enter для продолжения...")

if __name__ == "__main__":
    main()
