def string(str_1):
    count_upper = 0
    count_lower = 0
    for i in str_1:
        if i.isupper():

            count_upper += 1
        else:
            if i.islower():
                count_lower += 1
    print(f" upper case: {count_upper} \n lower case: {count_lower}")


string("The quick Brow Fox")
