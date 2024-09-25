list = []
while True:
    print('Grocery List Manager!')
    print('------------------------------')
    print()
    print('Choose an Option')
    print('1. Add an item')
    print('2. View the item')
    print('3. Remove an item')
    print('4. Exit')
    choice = int(input('Choice: '))

    match choice:
        case 1: 
            x = input('What item ')
            list.append(x)
            print(list)
        case 2: print(list)
        case 3: 
            print(list)
            y = input('What item are you removing')
            list.remove(y)
            print('item Removed')
        case 4: 
            print('End game')
            break
        case _: print('watdesigma')
