with open('input.txt', 'r') as f:
    data = f.read()
    arr = data.split()
    twice = 0
    thrice = 0
    for i in arr:
        for j in i:
            if i.count(j) == 2:
                twice += 1
                break
        for j in i:
            if i.count(j) == 3:
                thrice += 1
                break
    print(str(twice) + ' * ' + str(thrice) + ' = ' + str(twice * thrice))