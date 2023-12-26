
num_elements = int(input("Enter the number of elements in the list: "))

user_list = []

for _ in range(num_elements):
    element = input("Enter an element: ")
    user_list.append(element)

print("List created successfully:", user_list)
