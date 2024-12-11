file1 = open("Input.txt", "r")
data = file1.readline()
file1.close()
i = 0
bData = []
fileBlock = []
emptyBlock = []

while i <= len(data):
    fileBlock.append(data[i])
    if i!=len(data)-1:
        emptyBlock.append(data[i+1])
    i += 2

for i in range(0, len(fileBlock), 1):
    for j in range(0, int(fileBlock[i]), 1):
        bData.append(i)
    if i != len(emptyBlock):
        for j in range(0, int(emptyBlock[i]), 1):
            bData.append(".")

nData = []
count = 0
cData = 0
cDots = 0
bNum = []

for i in range(len(bData)-1, -1, -1):
    if bData[i] != ".":
        bNum.append(bData[i])
j = 0

for i in range(0, len(bNum), 1):
    if bData[i] != ".":
        nData.append(bData[i])
    else:
        nData.append(bNum[j])
        j+=1

total = 0

for i in range(0, len(nData), 1):
    total = total + (i*int(nData[i]))
print(total)