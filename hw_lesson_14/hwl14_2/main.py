from student import Student
from group import Group
from group_limit_reached_exception import GroupLimitReachedException

def main():
    try:
        st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
        st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
        gr = Group('PD1')
        gr.add_student(st1)
        gr.add_student(st2)
        print(gr)
        assert gr.find_student('Jobs') == st1  # 'Steve Jobs'
        assert gr.find_student('Jobs2') is None

        gr.delete_student('Taylor')
        print(gr)  # Only one student
    except GroupLimitReachedException as error:
        print(error)
    except Exception as error:
        print(error)

if __name__ == '__main__':
    main()