
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __del__(self,title,author ,year):
        return f"Deleted book with {self.title} --> {self.author}->{self.year} by {self.author}->{year} "
    def __repr__(self):
        return f"Book({self.title}, {self.author}, {self.year})"