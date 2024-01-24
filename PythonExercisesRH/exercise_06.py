row_number = int(input("Enter a row num (1-5): "))
column_number = int(input("Enter a column num (1-5): "))

if 1 <= row_number <= 5 and 1 <= column_number <= 5:
    for i in range(1, 6):
        for j in range(1, 6):
            if i == row_number and j == column_number:
                print(1, end=' ')
            else:
                print(0, end=' ')
        print()
else:
    print("Invalid input. Row and column numbers must be between 1 and 5 inclusive.")
    #I know we weren't supposed to do checking for right input but I forgot and did it anyway