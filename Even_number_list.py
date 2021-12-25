def even_num_list(lst):
    even_box = []
    for i in lst:
        if i % 2 == 0:
            even_box.append(i)
    print(even_box)


even_num_list([1, 2, 3, 4, 5, 6, 7, 8, 9])
