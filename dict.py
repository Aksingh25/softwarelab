
num_items = int(input("Enter the number of key-value pairs in the dictionary: "))


user_dict = {}

for _ in range(num_items):
    key = input("Enter a key: ")
    value = input("Enter a value: ")
    user_dict[key] = value

print("Dictionary created successfully:", user_dict)
