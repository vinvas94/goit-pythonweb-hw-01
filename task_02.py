import logging
from abc import ABC, abstractmethod

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(funcName)s - %(message)s")


class Book:
    def __init__(self, title: str, author: str, year: int) -> None:
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"title: {self.title}, author: {self.author}, year: {self.year}"


class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book):
        pass

    @abstractmethod
    def remove_book(self, title: str):
        pass

    @abstractmethod
    def show_books(self):
        pass


class Library(LibraryInterface):
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)
        logging.info(f"Added book: {book}")

    def remove_book(self, title: str):
        removed_books = [book for book in self.books if book.title == title]
        self.books = [book for book in self.books if book.title != title]
        for book in removed_books:
            logging.info(f"Removed book: {book}")

    def show_books(self):
        if not self.books:
            logging.info("Library is empty.")
        else:
            for book in self.books:
                logging.info(f"{book}")


class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self.library = library

    def run(self):
        while True:
            command = input("Enter command (add, remove, show, exit): ").strip().lower()

            if command == "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                try:
                    year = int(year)
                    self.library.add_book(Book(title, author, year))
                except ValueError:
                    logging.warning("Invalid year format. Please enter a valid integer.")
            elif command == "remove":
                title = input("Enter book title to remove: ").strip()
                self.library.remove_book(title)
            elif command == "show":
                self.library.show_books()
            elif command == "exit":
                break
            else:
                logging.warning("Invalid command. Please try again.")


if __name__ == "__main__":
    library = Library()
    manager = LibraryManager(library)
    manager.run()