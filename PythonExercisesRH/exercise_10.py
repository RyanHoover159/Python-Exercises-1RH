input_string = input("Enter a string: ")
characters_list = list(input_string)
nested_list = []

for i in range(0, len(characters_list), 3):
    nested_list.append(characters_list[i:i+3])

print("List of single characters:", characters_list)
print("List of lists with 3 elements each:", nested_list)