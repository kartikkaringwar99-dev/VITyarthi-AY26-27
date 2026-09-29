def library_summary(books):
    total = len(books)
    borrowed = sum(book["status"] == "Borrowed" for book in books)
    available = total - borrowed
    return {
        "total": total,
        "available": available,
        "borrowed": borrowed
    }
