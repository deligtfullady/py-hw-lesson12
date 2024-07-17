from logger import input_data, print_data
from change_delete import change_data, delete_data

def interface():
    print("Phonebook \n1 - write data \n2 - read data \n3 - change data \n4 - delete data")
    command = int(input('Enter number: '))

    while command != 1 and command != 2 and command != 3 and command != 4:
        print ('Incorrect input')
        command = int(input('Enter number: '))

    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        change_data()
    elif command == 4:
        delete_data()

