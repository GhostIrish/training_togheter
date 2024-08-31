from os import system
from sys import exit

# custom function to clear terminal
def clear_terminal():
    print()
    print("Press Enter")
    input()
    return system("cls")

# main loop
while True:
    menu = """
- CALCULATOR -
--------------
SUM = 1
SUBTRACT = 2
MULTIPLY = 3
DIVIDE = 4
EXIT = 5
--------------
    """
    print(menu)
    print()

    try:
        # get numbers from user
        num_1 = input("Value 1: ").upper()
        num_2 = input("Value 2: ").upper()
    
         # verify if numbers in num_1 and num_2 are float or integer.
        if "." in num_1 or "." in num_2:
            num_1 = float(num_1)
            num_2 = float(num_2)
        # limit user to use just '.' to declarate float numbers.      
        elif "," in num_1 or "," in num_2:
            print("For decimal numbers, use '.'")
            clear_terminal()
            continue      
        # else, numbers is considered integers.
        else:
            num_1 = int(num_1)
            num_2 = int(num_2)
            
        print()
        # get option for the menu
        option = int(input("Option: "))
        
        # use lambda functions to make math 
        if option == 1:
            print(f"Sum of values result in {(lambda x, y: x + y)(num_1, num_2)}") 
            # usei lambda para dificultar aqui nesses ifs, pra entenderam melhor o uso dele
            # em um exemplo simples, mas se você quiser, pode simplesmente fazer num_1 + num_2
            # e para os outros também.
            clear_terminal()
            
        if option == 2:
            print(f"Subtract of values result in {(lambda x, y: x - y)(num_1, num_2)}")
            clear_terminal()
            
        if option == 3:
            print(f"Multiply of values result in {(lambda x, y: x * y)(num_1, num_2)}")
            clear_terminal()
        
        if option == 4:
            print(f"Divide of values result in {(lambda x, y: x / y)(num_1, num_2)}")
            clear_terminal()

        if option == 5:
            print("Ok, Seeya :)")
            exit()
    # ensures the code to accept only numbers integers and floats.
    except ValueError:
        print("Type invalid.")
        clear_terminal()