
def prime_number(n):

    # logic for prime number or not
    if n == 1:
        return "1 is composite number"
    elif n == 2:
        return "Even prime number"
    else:
        for x in range(2, n):
            if n % x == 0:
                return "It is not prime number"
        return "It is prime number"


num = input("Enter the number: ")
print(prime_number(int(num)))

