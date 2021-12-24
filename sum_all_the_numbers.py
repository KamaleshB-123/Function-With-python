# sum all the numbers in a list

# create function definition

def sum_of_num(lst):
    add = 0
    for i in lst:
        add = add + i
    print(add)


arr = [8, 2, 3, 0, 7]
sum_of_num(arr)
