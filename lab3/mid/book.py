class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        return f"Book: '{self.title}', by author: {self.author}"

wp_book = Book("Война и мир","Лев Николаевич Толстой")
test_book = Book("Тестовая книга","Рощин Тимур")
print(wp_book)
print(test_book)