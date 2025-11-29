###
# Functions to read any data type from the keyboard
#
def input_string(message):
    value = input(message)
    return value

def input_integer(message):
    value = input(message)
    return int(value)

def input_real(message):
    value = input(message)
    return float(value)

def input_boolean(message):
    value = input(message)
    if value == "y":
        return True
    return False

###
# Allows to enter and print employee data. Due to personal
# data protection, you can determine whether information about
# the employee's salary will be printed
#
#import keyboard # your own defined module <-- tu chyba chodzi, żeby te funkcje powyżej zapisać w pliku "keyboard" ale kurwa to jest bez sensu w tym przypadku
#EDIT: Dokładnie o to chodzi z tym importem, ale nie chce mi się cofać z robieniem tego ścierwa xD jak ktoś chce to se przetestuje.

# Reads employee's data from keyboard
first_name = input_string('Enter name: ')
last_name = input_string('Enter last name: ')
age = input_integer('Enter age: ')
salary = input_real('Enter salary: ')
is_salary_hidden = input_boolean('Hide salary? (y/n)')

# Prints employee's record
print('DATA RECORD')
print('===========')
print('Name:', first_name, last_name)
print('Age:', age)
print('Salary:', 'HIDDEN' if is_salary_hidden else salary)
if is_salary_hidden:
    print('Salary')