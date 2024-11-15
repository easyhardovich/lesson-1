from group_limit_reached_exception import GroupLimitReachedException

class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"gender: {self.gender}, age: {self.age}, first_name: {self.first_name}, last_name: {self.last_name}"

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
        self.record_book = record_book

    def __str__(self):
        return f"gender: {self.gender}, age: {self.age}, first_name: {self.first_name}, last_name: {self.last_name}, last_name: {self.record_book}"

class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) < 10:
            self.group.add(student)
        else:
            raise GroupLimitReachedException("Досягнуто максимального значення групи", self.number)

    def delete_student(self, last_name):
        self.group.discard(self.find_student(last_name))

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student

    def __str__(self):
        all_students = ''
        for student in self.group:
            all_students += f"\nfirst_name: {student.first_name}, last_name: {student.last_name}"
        return f'Number:{self.number} {all_students} '
def main():
    st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
    st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN143')
    st3 = Student('Male', 26, 'Piter', 'Taylor', 'AN144')
    st4 = Student('Female', 24, 'Klara', 'Taylor', 'AN145')
    st5 = Student('Male', 27, 'Clark', 'Taylor', 'AN146')
    st6 = Student('Female', 25, 'Victoria', 'Taylor', 'AN147')
    st7 = Student('Male', 28, 'Victor', 'Taylor', 'AN148')
    st8 = Student('Female', 23, 'Anny', 'Taylor', 'AN149')
    st9 = Student('Male', 23, 'Larry', 'Taylor', 'AN150')
    st10 = Student('Female', 21, 'Omilia', 'Taylor', 'AN151')
    st11 = Student('Male', 26, 'Ozzi', 'Taylor', 'AN152')

    gr = Group('PD1')
    try:
        gr.add_student(st1)
        gr.add_student(st2)
        gr.add_student(st3)
        gr.add_student(st4)
        gr.add_student(st5)
        gr.add_student(st6)
        gr.add_student(st7)
        gr.add_student(st8)
        gr.add_student(st9)
        gr.add_student(st10)
        gr.add_student(st11)
    except GroupLimitReachedException as error:
        print(error)
    except Exception as error:
        print(error)
    print(gr)

if __name__ == '__main__':
    main()