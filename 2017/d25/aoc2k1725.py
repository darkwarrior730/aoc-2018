data = open('input1234567890.txt', 'r').read().split('\n')

state = data[0][15:16]
diognum = int(data[1][36:-7])
#print(state)
#print(diognum)

arr = [0]
position = 0

startoff = 2

func = {}

def runFunc():
    global arr
    global position
    global func
    global state
    if position == 0:
        arr = [0] + arr
        position += 1
    if position == len(arr)-1:
        arr = arr + [0]
    ta = func[state][str(arr[position])]
    arr[position] = int(ta[0])
    position += int(ta[1])
    state = ta[2]


for i in range(int((len(data)-startoff)/10)):
    curoff = startoff+1 + (10*i)
    statename = data[curoff][9:10]
    tempdict = {}
    for i in range(2):
        temp1 = data[curoff+1+(i*4)][26:27]
        temp2 = data[curoff+2+(i*4)][22:23]
        temp3 = 1 if data[curoff+3+(i*4)][27:] == 'right.' else -1
        temp4 = data[curoff+4+(i*4)][26:27]
        tempdict[temp1] = [temp2, temp3, temp4]
    func[statename] = tempdict

for i in range(diognum):
    runFunc()
    print(i)

num = 0
for i in arr:
    if i == 1:
        num += 1
print(num)