from Search_Methods import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort
from random import randint
import time

print("Welcome to the sort generator")
arr = []


def menu():
    print("""
    Enter 1 to use bubble sort,
    Enter 2 to use selection sort,
    Enter 3 to use insertion sort,
    Enter 4 to use merge sort,
    Enter 5 to use quick sort.
    Enter 6 to exit
    """)
    answer = int(input(">"))
    while answer <= 1 >= 6:             # This is the infinite loop
        menu()
    if answer == 1:
        print("You chose bubble sort.")
        number = int(input("How many numbers would you like to sort?>"))
        print(f"Ok so there will be {number} numbers randomly generated from 1-100,000 and added to this list")
        print("Give me a couple seconds will ya??")
        time.sleep(2)
        for x in range(number):         # gets the number from the user and runs the randint as many times as specified
            arr.append(randint(1, 100000))
        print("Here is your list",
              arr)              # Shows the array before the sort
        input("Press enter to sort!")
        bubble_sort(arr)        # shows the array after the sort, # Calls the bubble_sort method from Search_methods.py
        print("Here is your list sorted using the bubble sort method!")
        print(arr)
        return arr.clear(), input("Enter to continue"), menu()
    elif answer == 2:
        print("You chose selection sort.")
        number = int(input("How many numbers would you like to sort?>"))
        print(f"Ok so there will be {number} numbers randomly generated from 1-100,000 and added to this list")
        print("Give me a couple seconds will ya, I hate being rushed!!")
        time.sleep(2)           # calls the time function  imported
        for num in range(number):
            arr.append(randint(1, 100000))          # Calls the randint function imported
        print("Here is your list",
              arr)
        input("Press enter to sort!")
        selection_sort(arr)         # Calls the selection_sort method from Search_methods.py
        print(arr)
        return arr.clear(), input("Enter to continue"), menu()
    elif answer == 3:
        number = int(input("How many numbers would you like to sort?>"))
        print(f"Ok so there will be {number} numbers randomly generated from 1-100,000 and added to this list")
        print("Give me a couple seconds will ya, I hate being rushed!!")
        time.sleep(2)
        for num in range(number):
            arr.append(randint(1, 100000))
        print("Here is your list",
              arr)
        input("Press enter to sort!")
        insertion_sort(arr)     # Calls the insertion_sort method from Search_methods.py
        print(arr)
        return arr.clear(), input("Enter to continue"), menu()
    elif answer == 4:
        number = int(input("How many numbers would you like to sort?>"))
        print(f"Ok so there will be {number} numbers randomly generated from 1-100,000 and added to this list")
        print("Give me a couple seconds will ya, I hate being rushed!!")
        time.sleep(2)
        for num in range(number):
            arr.append(randint(1, 100000))
        print("Here is your list",
              arr)
        input("Press enter to sort!")
        merge_sort(arr)       # Calls the merge_sort method from Search_methods.py
        print(arr)
        return arr.clear(), input("Enter to continue"), menu()
    elif answer == 5:
        number = int(input("How many numbers would you like to sort?>"))
        print(f"Ok so there will be {number} numbers randomly generated from 1-100,000 and added to this list")
        print("Give me a couple seconds will ya, I hate being rushed!!")   # I really do hate being rushed, Thanks for giving us the weekend
        time.sleep(2)
        for num in range(number):
            arr.append(randint(1, 100000))
        print("Here is your list",
              arr)
        input("Press enter to sort!")
        quick_sort(arr)         # Calls the quick_sort method from Search_methods.py
        print(arr)
        return arr.clear(), input("Enter to continue"), menu()   # Clears the list and reruns the menu
    else:
        if answer == 6:
            exit("I didn't wanna sort for you anyway.")   # tells the user that it doesnt wanna sort for them anyway!!!!!


menu()
