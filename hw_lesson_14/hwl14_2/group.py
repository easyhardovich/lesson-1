from group_limit_reached_exception import GroupLimitReachedException
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