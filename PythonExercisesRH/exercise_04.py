n = int(input("Enter the number of floats: "))
float_list = []

for i in range(n):
    float_input = float(input(f"Enter float #{i + 1}: "))
    float_list.append(float_input)


mean = sum(float_list) / n
print("List:", float_list)
print("Average:", mean)