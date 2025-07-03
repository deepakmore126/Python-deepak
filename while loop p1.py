# function to print multification table
def print_table(number):
    i = 1 #start from 1
    while i <=10:
        print(f"{number} X {number * i}")
        i+= 1  # Increment Counter

        # Take Input from user
        num = int(input("Enter a number to print its table: "))

        # Call the function 
        print_table(num)

        take_input()