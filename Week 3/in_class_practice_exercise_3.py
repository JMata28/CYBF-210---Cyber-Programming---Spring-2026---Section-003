class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

def display_books(books):
    print("\nThese are the available books: ")
    for book in books:
        print(f"\"{book.title}\" by {book.author}")

def checkout_books(books):
    while(True):
        answer = input("\nPlease eenter the title of the book you'd like to check out: ")
        titles = []
        for book in books:
            titles.append(book.title.lower())
        if answer.lower() in titles:
            print(f"The book: {answer.title()} is available and is now checked out to you!\n")
            for book in books:
                if (book.title.lower() == answer.lower()):
                    books.remove(book)
                    break
            break
        else:
            print("The book you entered is not available.")

def main():
    book_1 = Book("The Lion, The Witch, and The Wardrobe", "C.S. Lewis")
    book_2 = Book("The Last Sin Eater", "Francine Rivers")
    book_3 = Book("Little Women", "Louisa may Alcott")
    books = [book_1, book_2, book_3]
    display_books(books)
    checkout_books(books)
    display_books(books)

main()