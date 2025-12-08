# class definition
class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.poor = True

def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student3 = Student()
    student1.name = "Dominic"
    student1.age = 19
    student1.poor = True
    student2.name = "Olivia"
    student2.age = 21
    student2.poor = False
    student3.name = "Eugeniusz"
    student3.age = 20
    student3.poor = True

    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name}, {student1.age} years old. Is the student poor? {student1.poor}')
    print(f'{student2.name}, {student2.age} years old. Is the student poor? {student2.poor}')
    print(f'{student3.name}, {student3.age} years old. Is the student poor? {student3.poor}')

if __name__ == "__main__":
    main()