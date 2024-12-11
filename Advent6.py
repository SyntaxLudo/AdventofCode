file1 = open("Input.txt", "r")
lines = file1.readlines()
file1.close()
count = 0
x = 0
y = 0

for i in range(0, len(lines), 1):
    new = []
    for j in range(0, len(lines[i]), 1):
        if (lines[i])[j] == "^":
            y = i
            x = j
        if (lines[i])[j] != "\n":
            new.append((lines[i])[j])
        #print(lines[y])
        #print(new)
    lines[i] = new
    del new

flag = False

while y!=0:
    while (lines[y])[x] != "#":
        new = []
        for i in range(0, len(lines[y]), 1):
            print(y)
            if (lines[y-1])[i] == "#" and i == x and y>=0:
                new.append("^")
            elif i == x and y>=0:
                new.append("X")
            else:
                new.append((lines[y])[i])
        lines[y] = new
        del new
        #print(y)
        y -= 1
        if y < 0:
            flag = True

    newGrid = []

    for i in range(len(lines[0])-1, -1, -1):
        new = []
        for j in range(0, len(lines), 1):
            new.append((lines[j])[i])
        newGrid.append(new)
        del new

    lines = newGrid
    del newGrid

    for i in range(0, len(lines), 1):
        for j in range(0, len(lines[i]), 1):
            if (lines[i])[j] == "^":
                y = i
                x = j
    #for i in range(0, len(lines), 1):
        #print(lines[i])
    #print("-----------------------------------------------------")
    if flag:
        y=0

count = 0

for i in range(0, len(lines), 1):
    for j in range(0, len(lines[i]), 1):
        if (lines[i])[j] == "X":
            count += 1




#for i in range(0, len(lines), 1):
    #print(lines[i])




print(count)