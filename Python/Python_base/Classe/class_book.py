class Book:
    TYPES=("hardcover","paperback ")
    
    def __init__(self,name,book_type,weight):
        self.name = name
        self.book_type=book_type
        self.weight=weight
        
    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weight:{self.weight}g>"
    
    def __str__(self):
        return f"The Book {self.name} is a {self.book_type},weighting {self.weight}g."
    
    @classmethod
    #This is how to create a new object inside a class
    def hardcover(cls, name, page_weight):
        return Book(name, Book.TYPES[0], page_weight+100)
    
    @classmethod
    # Classmethod is a direct access to the class
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight) #use cls instead of Book is better

#book = Book("Harry Potter","hardcover",1500)

book=Book.hardcover("Harry Potter", 1500)
light = Book.paperback("Python basics", 600)
print(book) #The Book Harry Potter is a hardcover, weighting 1600g.
print(light) #The Book Python basics is a paperback ,weighting 600g.

