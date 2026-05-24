import json
import os
from typing import List
from models import Book

STORAGE_FILE = "books.json"

def load_books() -> List[Book]:
    if not os.path.exists(STORAGE_FILE):
        return []
    with open(STORAGE_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    return [Book.from_dict(item) for item in data]

def save_books(books: List[Book]) -> None:
    data = [book.to_dict() for book in books]
    with open(STORAGE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def add_book(book: Book) -> bool:
    books = load_books()
    for existing in books:
        if existing.author == book.author and existing.title == book.title:
            return False
    books.append(book)
    save_books(books)
    return True

def delete_book(author: str, title: str) -> bool:
    books = load_books()
    for i, book in enumerate(books):
        if book.author == author and book.title == title:
            del books[i]
            save_books(books)
            return True
    return False
