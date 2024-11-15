from human import Human
class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"gender: {self.gender}, age: {self.age}, first_name: {self.first_name}, last_name: {self.last_name}, last_name: {self.record_book}"