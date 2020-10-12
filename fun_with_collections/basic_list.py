"""

Program: basic_list.py

Author: Donald Butters

Last date modified: 10/12/2020

The purpose of the program is to ask for three inputs from the user
and to output the numbers entered as a list


 :param parameter_1: ask for input
 :param parameter_2: assign to list
 :returns: prints list

 """

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
