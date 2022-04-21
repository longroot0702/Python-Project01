'''
- File Name: print_function.py
- Writer: Geunyoung kim
- Update Information: [2022, 04, 21] File Version 1.0
'''

# Print Menu
def menu():
    print("---------------------Menu---------------------\n")
    print("1. Print N Times Table")
    print("2. Print 2 ~ 19 Times Table")
    print("3. Exit")
    print("----------------------------------------------")

# Print N Times Table
def printN():
    print("----------------------------------------------\n")
    print("          [Print N Times Table]\n")
    
    while True:

        try:
            number = int(input("Please enter a number(2 ~ 19): "))
        except ValueError:
            print("\nError: Illegal Selection..\n")
        else:
            if number > 1 and number < 20:
                break
            else:
                print("\nError: Illegal Selection..\n")

    print("\n---------------%d Times Table---------------\n" %int(number))
    for each in range(2, 20):
        print('\t \t %d X %d = %d' %(number, each, number * each))
    print("----------------------------------------------\n")

# Print 2 ~ 19 Times Table
def printAll():
    print("----------------------------------------------")
    print("\n          [Print 2 ~ 19 Times Table]      \n")

    for item in range(2, 19, 3):
        for each in range(2, 20):
            print('%d X %d = %d\t%d X %d = %d\t%d X %d = %d' %(item, each, item * each, item + 1, each, (item + 1) * each, item + 2, each, (item + 2) * each))
        print("")
            
    print("----------------------------------------------\n")