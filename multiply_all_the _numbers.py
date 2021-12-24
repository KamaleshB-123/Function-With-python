
def mul_of_numbers(lst):
    product = 1
    for i in lst:
        product = i * product
    return product


arr = [8, 2, 3, -1, 7]
print(mul_of_numbers(arr))
