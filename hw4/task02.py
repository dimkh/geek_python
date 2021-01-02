orig_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [orig_list[i] for i in range(len(orig_list))
            if orig_list[i] > orig_list[i-1] and i > 0]

print(new_list)