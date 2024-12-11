file1 = open("Input.txt", "r")
lines = file1.readlines()
file1.close()
count = 0
rules = []
data = []
newData = []
swaps = 0

for line in range(0, len(lines), 1):
    count+=1
    rules.append(lines[line])
    if len(lines[line].strip()) == 0:
        break
for line in range(count, len(lines), 1):
    data.append(lines[line])

count = 0
currentBook=[]
for booklet in range(0, len(data), 1):
    pageNumber = -1
    reset = True
    currentBook = data[booklet].split(",")
    while pageNumber < len(currentBook)-1:
        pageNumber += 1
        for rule in range(0, len(rules) - 1, 1):
            reset = False
            page = rules[rule].split("|")
            if int(currentBook[pageNumber]) == int(page[0]):
                for previousPages in range(0, pageNumber, 1):
                    if int(currentBook[previousPages]) == int(page[1]):
                        currentBook[pageNumber] = page[1]
                        currentBook[previousPages] = page[0]
                        pageNumber = 0
                        swaps += 1
                        reset = True
                        break
            if reset:
                continue

    count += int(currentBook[int((len(currentBook) - 1) / 2)])
    print(currentBook)
    print (count, " --- ", booklet, " --- ", int(currentBook[int((len(currentBook) - 1) / 2)]))

print(count)
print(swaps)