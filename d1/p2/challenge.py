with open('input.txt', 'r') as f:
    data = f.read()
    arr = data.split()
    arr2 = [0]
    number = 0
    while True:
        for i in arr:
            number += int(i)
            if number in arr2:
                print(number)
                quit()
            else:
                arr2.append(number)
