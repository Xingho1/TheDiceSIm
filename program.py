import functions

feedback = 0
number_of_dice = 1

print("""Welcome to Dice roller...\n
    > Type 'config' for the configuration of dice.\n
    > Type 'roll' to roll the dice.\n
    > Type 'quit' to exit the program.""")

while True:
    command = input(">>").lower().strip()

    if command == 'roll':
        print(functions.roll())
    elif command == 'config':
        number_of_dice = input("Enter the number of dice you want to include:")
        if number_of_dice.isnumeric() is True :
            functions.config(number_of_dice)
        else:
            print("Not numeric.")
    elif command == 'quit':
        print("Thanks for using our service, we hope you liked it.")
        feedback = input("Rate us out of five:")
        break
    else:
        print("Sorry but are unable to recognise such command.")
 
