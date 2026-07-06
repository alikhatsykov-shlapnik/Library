class Book:
    """Класс для предоставления книги"""

    def __init__(self, title: str, auther: str, year: int, book_id: int = None, status: str = "В наличии"):
        self.id = book_id
        self.title = title
        self.auther = auther
        self.year = year
        self.status = status

    def __str__(self):
        """Строковое представление книги (для print)"""
        return f"[{self.id}], {self.title} - {self.auther} ({self.year}) - {self.status}"

    def __repr__(self):
        """Представление для Разработчиков"""
        return f"Book(id = {self.id}, title = '{self.title}', author = '{self.auther}', year = '{self.year}', status = '{self.status}')"
    
    def to_dict(self):
        """превращает книгу в словарь"""
        return {
            "id": self.id,
            "title": self.title,
            "author": self.auther,
            "year": self.year,
            "status": self.status
        }