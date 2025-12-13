class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (f"Biblioteka: {self.city}, {self.street}, {self.zip_code}\n"
                f"Godziny otwarcia: {self.open_hours}, Tel: {self.phone}")


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date,
                 city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (f"Pracownik: {self.first_name} {self.last_name}\n"
                f"Zatrudniony od: {self.hire_date}, ur.: {self.birth_date}\n"
                f"Adres: {self.city}, {self.street}, {self.zip_code}, Tel: {self.phone}")


class Book:
    def __init__(self, library, publication_date, author_name,
                 author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (f"Książka: {self.author_name} {self.author_surname}\n"
                f"Data publikacji: {self.publication_date}, Stron: {self.number_of_pages}\n"
                f"{self.library}")


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_str = "\n\n".join(str(book) for book in self.books)
        return (f"Zamówienie z dnia: {self.order_date}\n\n"
                f"{self.student}\n\n"
                f"Obsługujący pracownik:\n{self.employee}\n\n"
                f"Książki:\n{books_str}\n"
                f"{'-'*40}")
