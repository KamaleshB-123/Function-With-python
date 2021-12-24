
def test_range(n):
    if n in range(3, 9):
        print("%s is in the range" % str(n))
    else:
        print("The number is outside the given range.")


a = int(input("Enter your number: "))
test_range(a)
