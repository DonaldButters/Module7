"""

Program: function_key.py

Author: Donald Butters

Last date modified: 10/12/2020

The purpose of the program is to make three function calls each with different number of scors and key word arguments
and to output the numbers entered as a list


 :param parameter_1: use arbitrary arguments list and keyword arguments
 :param parameter_2: make 3 function calls to each
 :returns: a string in a specific format

 """

def average_steps(*args, **kwargs):
    # Use *args for average calculation
    total = 0
    items = 0
    print('Pedometer Results: ')
    for key, value in kwargs.items():
        print(str(key) + ' - ' + str(value))

        #print("%s == %s" % (key, value))
    for i in args:
        total = total + int(i)
        items = items + 1
        #print(str(total))

    average = total / items

    print('Your average steps over the past ' + str(items) + ' days is: ' + str(average))

    # return


if __name__ == 'main':
    print(average_steps(2501, 6789, 8952, 40145, 10995, 23914, weight='169', name='Donald', age='77'))
    print(average_steps(17125, 15622, 23584, weight='230', name='Daniel'))
    print(average_steps(500, 500, 500, 500, weight='419', name='Tubby', exwives='55'))

