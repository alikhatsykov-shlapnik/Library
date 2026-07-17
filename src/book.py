class Book:
    """Класс для предоставления книги"""

    def __init__(self, title: str, author: str, year: int, book_id: int = None, status: str = "В наличии"):
        self.id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def __str__(self):
        """Для пользователей"""
        return f"[{self.id}], {self.title} - {self.author} ({self.year}) - {self.status}"

    def __repr__(self):
        """Для Разработчиков"""
        return f"Book(id = {self.id}, title = '{self.title}', author = '{self.author}', year = '{self.year}', status = '{self.status}')"
    
    def to_dict(self):
        """превращает книгу в словарь"""
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }