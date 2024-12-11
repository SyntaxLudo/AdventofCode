
file1 = open("Input.txt", "r")
data = file1.readline()
file1.close()
stones = data.split()

for a in range(0, 25, 1):
    newStones = []
    print(a)
    for i in range(0, len(stones), 1):
        if stones[i] == "0":
            newStones.append("1")
        elif len(stones[i])%2 == 0:
            stone = stones[i]
            stone1 = stone[:int(len(stone)/2)]
            stone2 = stone[int(len(stone) / 2):]
            newStones.append(str(stone1))
            stone22 = str(stone2).lstrip("0")
            if stone22 == "":
                newStones.append("0")
            else:
                newStones.append(stone22)
        else:
            newStones.append(str(int(stones[i])*2024))
    stones = newStones
    del newStones

print(len(stones))
