import re

file1 = open("Input.txt", "r")
lines = file1.readlines()
file1.close()
pattern = re.compile(r'mul\(\d+,\d+\)')
code = "".join(lines)
data = []
search = pattern.finditer(code)
count = -1
total = 0
flag = []
safe = False

for i in search:
    data.append(i.group())
    count+=1
    #print(data[count])



for i in range(0, len(data), 1):
    current = (((data[i].split("mul("))[1]).split(")"))[0].split(",")
    total = total + (int(current[0])*int(current[1]))

print(total)
