def make_list():
    for i in range(0, 3):
        a = get_input()
        input_list.append(a)
    print(input_list)
    return input_list

def get_input():
    data = input('Please enter a number: ')
    return data


input_list = []
make_list()
