
num_elements = int(input("Enter the number of elements in the tuple: "))


temp_list = []


for _ in range(num_elements):
    element = input("Enter an element: ")
    temp_list.append(element)

user_tuple = tuple(temp_list)

print("Tuple created successfully:", user_tuple)
