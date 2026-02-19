class Library_Item:
    def __init__(self, type, title, checked_out_status):
        self.type = type
        self.title= title
        self.status = checked_out_status

    def checkout(self):
        if ( self. status == True):
            print(f"This {self.type} is already checked out.")
        else:
            print(f"This {self.type} is available for checkout.")

class Book(Library_Item):
    def __init__(self, type, title, checked_out_status, author, publisher):
        super().__init__(type, title, checked_out_status)
        self.author = author
        self.publisher = publisher
    
    def display_book(self):
        print(f"The {self.type}'s title is \"{self.title}\" by {self.author}, published by {self.publisher}.")
        
class Movie(Library_Item):
    def __init__(self, type, title, checked_out_status, director, lead_actors=None):
        super().__init__(type, title, checked_out_status)
        self.director = director 
        if (lead_actors == None):
            self.lead_actors = []
        else:
            self.lead_actors = lead_actors
    def display_movie(self):
        print(f"The {self.type}'s title is \"{self.title}\", directed by {self.director} and starring:")
        for actor in self.lead_actors:
            print(actor)

book_1 = Book("book", "Moby Dick", False, "Herman Melville", "Penguin Classics")
book_1.display_book()
book_1.checkout()

movie_1 = Movie("movie", "No Way Home", True, "Sam Raimi", ["Tom Holland", "Tobey Maguie", "Andrew Garfield"])
movie_1.display_movie()
movie_1.checkout()