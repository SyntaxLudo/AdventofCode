file1 = open("Input.txt", "r")
data = file1.readlines()
file1.close()
count = 0
lines = []

for i in range(0, len(data), 1):
    temp=[]
    for j in range(0,len(data[i]), 1):
        if (data[i])[j] != '\n':
            temp.append((data[i])[j])
    lines.append(temp)
    del temp

aNode = []
for i in range(0,len(lines),1):
    for j in range(0, len(lines[i]), 1):
        if (lines[i])[j] != ".":
            for a in range(0, len(lines), 1):
                for b in range(0, len(lines[a]), 1):
                    if (lines[i])[j] == (lines[a])[b] and not(i==a and j==b):
                        if a < i:
                            difX=abs(a-i)
                            difY = abs(b - j)
                            if b < j:
                                if a-difX>=0 and b-difY>=0:
                                    count+=1
                                    if (str(a-difX),",",str(b-difY)) not in aNode:
                                        aNode.append((str(a-difX),",",str(b-difY)))
                            if b >= j:
                                if a-difX>=0 and b+difY<len(lines[i]):
                                    count+=1
                                    if (str(a - difX), ",", str(b + difY)) not in aNode:
                                        aNode.append((str(a - difX), ",", str(b + difY)))
                        if a >= i:
                            difX=abs(a-i)
                            difY = abs(b - j)
                            if b < j:
                                if a+difX<len(lines) and b-difY>=0:
                                    count+=1
                                    if (str(a + difX), ",", str(b - difY)) not in aNode:
                                        aNode.append((str(a + difX), ",", str(b - difY)))
                            if b >= j:
                                if a+difX<len(lines) and b+difY<len(lines[i]):
                                    count+=1
                                    if (str(a + difX), ",", str(b + difY)) not in aNode:
                                        aNode.append((str(a + difX), ",", str(b + difY)))

print(len(aNode))