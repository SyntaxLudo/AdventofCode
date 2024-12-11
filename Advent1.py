file1 = open("Input.txt", "r")
xup = file1.readlines()
file1.close()
count = 1

for i in range(0, len(xup), 1):
    for j in range(0, len(xup[i]), 1):
        if (xup[i])[j] == "0":
            x = i
            y = j
            for k in range(1,10,1):
                if int((xup[x+1])[y]) == k:
                    x+=1
                elif int((xup[x-1])[y]) == k:
                    x-=1
                elif (xup[x])[y+1] == str(k):
                    y+=1
                elif (xup[x])[y-1] == str(k):
                    y-=1
                else:
                    break
                if k == 9:
                    count+=1
print(count)



