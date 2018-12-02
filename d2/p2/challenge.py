with open('input.txt', 'r') as f:
    data = f.read()
    arr = data.split()
    length = len(arr[0])
    for i in arr:
        for j in arr:
            if arr.index(i) == arr.index(j):
                break
            num = 0
            string = ''
            for k in range(length):
                if i[k] != j[k]:
                    num += 1
                else:
                    string += i[k]
            if num == 1:
                print(i, j)
                print(string)
                quit()
