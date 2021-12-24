def find_max(a, b, c):

    if a > b and a > c:
        print(f"A=({a}) the greater than B=({b}) and C = ({c})")

    elif b > c:
        print(f"B=({b}) is greater than C=({c}) and A=({a})")

    else:
        print(f"C=({c}) is greater")


x = int(input("Enter the Number: "))
y = int(input("Enter the Numebr: "))
z = int(input("Enter the Number: "))
find_max(x, y, z)
