file1 = open("Input.txt", "r")
lines = file1.readlines()
file1.close()
count = 0
rules = []
data = []

for i in range(0, len(lines), 1):
    count+=1
    rules.append(lines[i])
    if len(lines[i].strip()) == 0:
        break
for i in range(count, len(lines), 1):
    data.append(lines[i])

count = 0
print(data)
currentData=[]

for i in range(0, len(data), 1):
    valid = True
    currentData = data[i].split(",")
    for j in range(0, len(rules)-1, 1):
        num = rules[j].split("|")
        for k in range(0, len(currentData), 1):
            if int(currentData[k]) == int(num[0]):
                for l in range(0, k, 1):
                    if int(currentData[l]) == int(num[1]):
                        valid = False
    if valid:
        count += int(currentData[int((len(currentData)-1)/2)])

print(count)