def read_data(file_path, file_num):
    if file_num == 1:
        with open(file_path, 'r', encoding='utf-8') as f:
            data_first = f.readlines()
            data_first_list = []
            j = 0
            for i in range(len(data_first)):
                if data_first[i] == '\n' or i == len(data_first) - 1:
                    data_first_list.append(''.join(data_first[j:i+1])) # запись [j:i+1] - срез
                    j = i
            return data_first_list
    elif file_num == 2:
        with open(file_path, 'r', encoding='utf-8') as f:
            data_second = f.readlines()
            data_second_list = []
            for i in range(len(data_second)):
                if data_second[i] != '\n':
                    data_second_list.append(data_second[i])
            return data_second_list

def print_data(data):
    data_len = len(data)
    # print (data_len)
    if data_len < 1:
        return 0
    for i in range(data_len):
        # добавить проверку на длину файла, если данных нет, то выводить сообщение!
        if data[i][0] == '\n':
            print(f"{i+1}{data[i]}")
        else:
            print(f"{i+1}\n{data[i]}")
    block = int(input('Enter number of block you want to change or delete: '))
    while block <= 0 or block > data_len:
        print ('Incorrect input')
        block = int(input('Enter number: '))
    return block
        

def write_data(file_path, data):
        open(file_path, 'w').close()
        with open(file_path, 'a', encoding='utf-8') as f:
            f.write(''.join(data))


# print_data(read_data('data_first.csv', 1))
# print_data(read_data('data_second.csv', 2))