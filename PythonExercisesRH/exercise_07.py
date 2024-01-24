numbers_list = []
even_numbers_list = []

while True:
    user_input = input("Enter a number or QUIT to quit: ")

    if user_input.upper() == "QUIT":
        break

    if(not user_input.isdigit()):
        print("Invalid input. Please enter a number.")    
        #I know we weren't supposed to do checking for right input but I forgot and did it anyway
    else:
        number = int(user_input)
        numbers_list.append(number)

    if number % 2 == 0:
        even_numbers_list.append(number)

# Print both lists
print("List of all numbers:", numbers_list)
print("List of even numbers:", even_numbers_list)
