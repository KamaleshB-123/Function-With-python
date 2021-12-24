def unique_elements(l1):
    org_box = []
    for i in l1:
        if i not in org_box:
            org_box.append(i)
    print(org_box)


unique_elements([1, 2, 3, 3, 3, 3, 4, 5])
