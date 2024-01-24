string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if (string1.endswith(string2)):
    print("True")
    
elif (string2.endswith(string1)):
    print("True")

else:
    print("False")