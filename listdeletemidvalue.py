def delete_middle_element(my_list):

    middle_index = len(my_list) // 2

    if len(my_list) % 2 == 1:
        del my_list[middle_index]
        print("Middle element deleted successfully.")
        return my_list
    else:
        print("The list has an even number of elements. No middle element to delete.")
        return my_list


my_list = [1, 2, 3, 4, 5]
print("Original List:", my_list)

my_list = delete_middle_element(my_list)
print("List after deleting middle element:", my_list)
