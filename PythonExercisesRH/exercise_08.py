numbers_list = []
unique_elements_list = [element for element in numbers_list if numbers_list.count(element) == 1]

for i in range(10):
    numbers_list.append(int(input("Enter number: ")))

unique_elements_list = [element for element in numbers_list if numbers_list.count(element) == 1]

print("Original list:", numbers_list)
print("Nums that appear once:", unique_elements_list)
