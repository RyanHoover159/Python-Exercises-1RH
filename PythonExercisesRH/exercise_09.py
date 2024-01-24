words_list = []

for i in range(5):
    words_list.append(input(f"Enter word #{i + 1}: "))

result_string = ' '.join(words_list)

print("List of words:", words_list)
print("Resultant string:", result_string)