class Book:
    def __init__(self, title, author, isbn, availability=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.__availability = availability

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Availability: {'Available' if self.__availability else 'Not Available'}")

    def get_availability(self):
        return self.__availability

  
    def set_availability(self, availability):
        self.__availability = availability


book1 = Book("Kirabo Phionah", "J.K. Rowling", "9780545790352")
book1.display_info()


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, title):
        self.books = [book for book in self.books if book.title != title]

    def list_books(self):
        for book in self.books:
            book.display_info()

    def search_book(self, query):
        found_books = [book for book in self.books if query.lower() in book.title.lower() or query.lower() in book.author.lower()]
        if found_books:
            print("Found books:")
            for book in found_books:
                book.display_info()
        else:
            print("No books found with the given query.")


# Example usage
library = Library()
library.add_book(book1)
library.list_books()
library.search_book("Rowling")


class Library:
    def __init__(self):
        self.books = []

    # Other methods omitted for brevity

    def checkout_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.get_availability():
                    book.set_availability(False)
                    print(f"Book '{title}' checked out successfully.")
                else:
                    print(f"Book '{title}' is not available for checkout.")
                return
        print(f"Book '{title}' not found in the library.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.set_availability(True)
                print(f"Book '{title}' returned successfully.")
                return
        print(f"Book '{title}' not found in the library.")



library = Library()
library.checkout_book("Harry Potter")
library.return_book("Harry Potter")


def main():
    library = Library()

    while True:
        print("\nWelcome to the Library System")
        print("1. Add a Book")
        print("2. List all Books")
        print("3. Search for a Book")
        print("4. Check Out a Book")
        print("5. Return a Book")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            isbn = input("Enter the ISBN of the book: ")
            book = Book(title, author, isbn)
            library.add_book(book)
            print("Book added successfully.")

        elif choice == "2":
            print("\nAll Books:")
            library.list_books()

        elif choice == "3":
            query = input("Enter the title or author to search for: ")
            library.search_book(query)

        elif choice == "4":
            title = input("Enter the title of the book to check out: ")
            library.checkout_book(title)

        elif choice == "5":
            title = input("Enter the title of the book to return: ")
            library.return_book(title)

        elif choice == "6":
            print("Exiting the Library System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
