for num in range(50):
    for val in range(2, num):
        for n in range(2, val):
            if (val % n) == 0:
                break
        else:
            print(val)