from typing import List
from models import Book

def calculate_average_rating(books: List[Book]) -> float:
    if not books:
        return 0.0
    total = sum(book.rating for book in books)
    return round(total / len(books), 2)

def get_stats_by_author(books: List[Book]) -> dict:
    stats = {}
    for book in books:
        if book.author not in stats:
            stats[book.author] = {"count": 0, "total_rating": 0}
        stats[book.author]["count"] += 1
        stats[book.author]["total_rating"] += book.rating

    result = {}
    for author, data in stats.items():
        result[author] = {
            "count": data["count"],
            "avg_rating": round(data["total_rating"] / data["count"], 2),
        }
    return result
