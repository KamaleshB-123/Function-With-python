

def factorial_number(num):
    fact = 1

    for i in range(1, num+1):
        fact = i * fact
        if num == 0:
            return 1
    return fact


print(factorial_number(5))
