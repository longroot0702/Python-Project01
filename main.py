'''
- File Name: main.py
- Writer: Geunyoung kim
- Update Information: [2022, 04, 21] File Version 1.0
'''

import print_function

while True:
    print_function.menu()

    try:
        choice = int(input("\nSelect the menu: "))
    except ValueError:
        print("\nError: Illegal Selection..\n")
    else:
        if choice == 1:
            print_function.printN()
        elif choice == 2:
            print_function.printAll()
        elif choice == 3:
            exit()
        else:
            print("\nError: Illegal Selection..\n")