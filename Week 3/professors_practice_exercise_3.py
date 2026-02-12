class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

def display_books(books):
    for book in books:
        print(f"\"{book.title}\" by {book.author}")

def checkout_book(books):
    while (True):
        answer = input("\nPlease enter the title of the book you'd like to check out: ")
        titles = [] 
        for book in books: 
            titles.append(book.title.lower()) #Fill the list "titles" with every book title in lowercase letters
        if answer.lower() in titles: #turn the user input into all lowercase for comparison purposes
            print(f"The book: {answer.title()} is available and is now checked out to you!\n")
            for book in books: #Find which item of type Book has the title that matches the answer and remove it from the list of available books
                if (book.title.lower()== answer.lower()):
                    books.remove(book)
                    break
            break
        else:
            print("The book you entered is not available.")

def main():
    book_1 = Book("The Lion, the Witch and the Wardrobe", "C.S. Lewis")
    book_2 = Book("The Last Sin Easter", "Francine Rivers")
    book_3 = Book("Little Women", "Louisa May Alcott")
    books = [book_1, book_2, book_3]
    print("\nThese are the available books: ")
    display_books(books)
    checkout_book(books)
    print("These are the available books: ")
    display_books(books)

main() #This calls the main function