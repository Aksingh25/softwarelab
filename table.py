def print_multiplication_table(number):
    print(f"Multiplication Table for {number}:")

    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")


table_number = int(input("Enter the number for the multiplication table: "))
print_multiplication_table(table_number)

