
list1 = []
list2 = []

for _ in range(5):
    list1.append(int(input("Enter integer for list 1: ")))

for _ in range(5):
    list2.append(int(input("Enter integer for list 2: ")))

common_list = list(set(list1) & set(list2))

print("List 1:", list1)
print("List 2:", list2)
print("Common List:", common_list)