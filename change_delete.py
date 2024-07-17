from read_write import read_data, write_data, print_data
from data_create import name_data, surname_data, phone_data, address_data

def change_contact (f):
    contact = ""
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    if f == 1:
        contact = f"{name}\n{surname}\n{phone}\n{address}\n\n"
    elif f == 2:
        contact = f"{name}; {surname}; {phone}; {address}\n\n"
    return contact

def change_data():
    data_list = []
    file = int(input("Enter number of file you want to work with: "))
        
    while file != 1 and file != 2:
        print ('Incorrect input')
        file = int(input('Enter number (1 or 2): '))

    if file == 1:
        data_list = read_data('data_first.csv', file)
    else:
        data_list = read_data('data_second.csv', file)

    chg_index = print_data(data_list)
    if (chg_index == 0):
        print ("Nothing to change. List of contacts is empty")
        return
    
    new_contact = change_contact(file)


    answ = str(input (f"You want to change record №{chg_index}? (y/n): "))
    while answ!="y" and answ!="Y" and answ!="n" and answ!="N":
        print ('Incorrect input')
        answ = str(input ("Enter 'y'(yes) or 'n'(no): "))
    
    if answ == 'n' or answ == "N":
        print ("No changes were made")
        return

    data_list[chg_index-1] = new_contact

    if file == 1:
        write_data('data_first.csv', data_list)
    else:
        write_data('data_second.csv', data_list)
    print (f"Record {chg_index} was changed")


def delete_data():
    data_list = []
    file = int(input("Enter number of file you want to work with: "))
        
    while file != 1 and file != 2:
        print ('Incorrect input')
        file = int(input('Enter number (1 or 2): '))

    if file == 1:
        data_list = read_data('data_first.csv', file)
    else:
        data_list = read_data('data_second.csv', file)

    del_index = print_data(data_list)
    if (del_index == 0):
        print ("Nothing to delete. List of contacts is empty")
        return
    
    answ = str(input (f"You want to delete record №{del_index}? (y/n): "))
    while answ!="y" and answ!="Y" and answ!="n" and answ!="N":
        print ('Incorrect input')
        answ = str(input ("Enter 'y'(yes) or 'n'(no): "))
    
    if answ == 'n' or answ == "N":
        print ("No changes were made")
        return

    del data_list[del_index-1]
    if file == 1:
        write_data('data_first.csv', data_list)
    else:
        write_data('data_second.csv', data_list)
    print (f"Record {del_index} was deleted")


# delete_data()
