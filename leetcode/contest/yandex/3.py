def remove_duplicate(ns):
    temp_list = []
    for i in range(0, ns):
        temp_list.append(int(input()))
    check_value = temp_list[0]
    while_end_counter = len(temp_list)
    delete_counter = 1
    next_counter = 1
    while while_end_counter > 1:
        if check_value == temp_list[delete_counter]:
            temp_list.pop(delete_counter)
        else:
            check_value = temp_list[next_counter]
            next_counter = next_counter + 1
            delete_counter = delete_counter + 1
        while_end_counter = while_end_counter - 1
    for i in temp_list:
        print(i)


n = int(input())
remove_duplicate(n)
