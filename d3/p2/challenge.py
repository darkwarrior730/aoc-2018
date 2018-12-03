arr = [['.' for i in range(1000)] for i in range(1000)]

with open('input.txt', 'r') as f:
    datat = f.read().split('\n')
    data = []
    for i in datat:
        id = i.split('@')[0][1:]
        left, top = i.split('@')[1].split(':')[0].split(',')[0], i.split('@')[1].split(':')[0].split(',')[1]
        wide, tall = i.split('@')[1].split(':')[1].split('x')[0], i.split('@')[1].split(':')[1].split('x')[1]
        data.append([id, left, top, wide, tall])

    corid = ''
    for i in data:
        id = i[0]
        loff = int(i[1])
        toff = int(i[2])
        w = int(i[3])
        t = int(i[4])
        for j in range(t):
            for k in range(w):
                if arr[toff+j][loff+k] == '.':
                    arr[toff+j][loff+k] = id
                else:
                    arr[toff+j][loff+k] = 'x'
    
    largeid = data[len(data)-1][0]
    arr2 = [0 for i in range(int(largeid))]

    for i in range(1000):
        for j in range(1000):
            if arr[i][j] != '.' and arr[i][j] != 'x':
                arr2[int(arr[i][j])-1] += 1

    for i in data:
        if arr2[int(i[0])-1] == int(i[3])*int(i[4]):
            print(i[0])
            quit()