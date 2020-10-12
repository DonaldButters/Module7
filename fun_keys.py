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

    return ('Your average steps over the past ' + str(items) + ' days is: ' + str(average))

    # return


if __name__ == 'main':
    print(average_steps(2501, 6789, 8952, 40145, 10995, 23914, weight='169', name='Donald', age='77'))
    print(average_steps(17125, 15622, 23584, weight='230', name='Daniel'))
    print(average_steps(500, 500, 500, 500, weight='419', name='Tubby', exwives='55'))
