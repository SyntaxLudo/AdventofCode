
file1 = open("Input.txt", "r")
data = file1.readline()
file1.close()
stones = data.split()
stoneNum = []
stoneOcc = []
track = []

for i in range(0, len(stones), 1):
    if stones[i] not in track:
        track.append(stones[i])
        count = 0
        for j in range(0, len(stones), 1):
            if stones[i] == stones[j]:
                count+=1
        stoneNum.append(stones[i])
        stoneOcc.append(count)
        del count
del track


for a in range(0, 75, 1):
    print(a)
    newStones = []
    newOcc = []
    for i in range(0, len(stoneNum), 1):
        if stoneNum[i] == "0":
            newStones.append("1")
            newOcc.append(stoneOcc[i])
        elif len(stoneNum[i])%2 == 0:
            stone = stoneNum[i]
            stone1 = stone[:int(len(stone)/2)]
            stone2 = stone[int(len(stone) / 2):]
            newStones.append(str(stone1))
            stone22 = str(stone2).lstrip("0")
            if stone22 == "":
                newStones.append("0")
            else:
                newStones.append(stone22)
            newOcc.append(stoneOcc[i])
            newOcc.append(stoneOcc[i])
        else:
            newStones.append(str(int(stoneNum[i])*2024))
            newOcc.append(stoneOcc[i])
    track = []
    del stoneNum, stoneOcc
    stoneNum, stoneOcc = [], []
    for i in range(0, len(newStones), 1):
        if newStones[i] not in track:
            track.append(newStones[i])
            count = 0
            otherCount = 0
            for j in range(0, len(newStones), 1):
                if newStones[i] == newStones[j]:
                    count += 1
                    otherCount = otherCount + newOcc[j]
            stoneNum.append(newStones[i])
            stoneOcc.append(otherCount)
    del newStones
getSum = 0

for i in range(0, len(stoneOcc), 1):
    getSum = getSum + stoneOcc[i]
print(getSum)
