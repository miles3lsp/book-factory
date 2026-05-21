import random


class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author


def generate_random_book():
    titles = ["1984", "The Hobbit", "Gatsby"]
    authors = ["Orwell", "Tolkien", "Fitzgerald"]

    return Book(random.choice(titles), random.choice(authors))


if __name__ == "__main__":
    book = generate_random_book()
    print(f"Book: {book.title} by {book.author}")