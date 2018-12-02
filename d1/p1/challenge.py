with open('input.txt', 'r') as f:
    data = f.read()
    arr = data.split()
    number = 0
    for i in arr:
        number += int(i)
    print(number)
