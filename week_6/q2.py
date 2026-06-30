class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def short_title(self):
        return self.title[:10]


book1 = Book("Python Programming", "John")
book2 = Book("Data Structures", "Alex")
book3 = Book("Artificial Intelligence", "David")

print(book1.short_title())
print(book2.short_title())
print(book3.short_title())