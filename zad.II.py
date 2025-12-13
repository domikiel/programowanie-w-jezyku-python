from datetime import date

class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (f"Biblioteka: {self.city}, {self.street}, {self.zip_code}\n"
                f"Godziny otwarcia: {self.open_hours}, tel: {self.phone}")

class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
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
                f"Adres: {self.city}, {self.street}, {self.zip_code}, tel: {self.phone}\n")

class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (f"Książka: {self.author_name} {self.author_surname}\n"
                f"Data publikacji: {self.publication_date}, stron: {self.number_of_pages}\n"
                f"{self.library}")

class Student:
    def __init__(self, first_name, last_name, student_id):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id

    def __str__(self):
        return f"Student {self.first_name} {self.last_name}, ID: {self.student_id}\n"

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
                f"Książki:\n{books_str}\n{'-'*50}")

library1 = Library("Katowice", "Testowa 1", "11-001", "10:00-18:00", "555444666")
library2 = Library("Tychy", "Wolności 5", "40-725", "9:00-17:00", "623326666")

employee1 = Employee("Hania", "Bania", date(2025, 1, 1), date (2000, 2, 11), "Katowice", "Rolna 1", "01-100", "587412589")
employee2 = Employee("Marek", "Nowak", date(2019, 7, 31), date (1975, 3, 25), "Tychy", "Fiołkowa 67", "43-100", "000111222")
employee3 = Employee("Jarek", "Kowalski", date(2010, 4, 10), date (1953, 6, 26), "Katowice", "Podleśna 99", "01-114", "595696434")

book1 = Book(library2, 1990, "Henryk", "Skorupa", 999)
book2 = Book(library2, 2010, "Adam", "Mickiewicz", 100)
book3 = Book(library1, 1989, "Olga", "Tokarczuk", 388)
book4 = Book(library2, 2020, "Mark", "Twain", 210)
book5 = Book(library1, 1995, "Lech", "Wałęsa", 88)

student1 = Student("Michał", "Kichał", "KARTA01")
student2 = Student("Karolina", "Lis", "KARTA02")
student3 = Student("Kornel", "Kajak", "KARTA03")

order1 = Order(employee1, student1, [book2, book5], date(2025, 11, 27))
order2 = Order(employee3, student2, [book1, book3, book4], date(2025, 12, 1))

print(order1)
print(order2)