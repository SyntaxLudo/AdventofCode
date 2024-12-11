file1 = open("Input.txt", "r")
reports = file1.readlines()
file1.close()
count=0
failReports = []



for i in range(0, len(reports), 1):
    safe = True
    levels = reports[i].split()
    for j in range(0, (len(levels) - 1), 1):
        if int(levels[0]) < int(levels[1]) and not(-3 <= int(levels[j]) - int(levels[j + 1]) <= -1):
            safe = False
        elif int(levels[0]) > int(levels[1]) and not(1 <= int(levels[j]) - int(levels[j + 1]) <= 3):
            safe = False
        elif int(levels[0]) == int(levels[1]):
            safe = False

    if safe:
        count+=1
    else:
        failReports.append(reports[i])
    del levels

for i in range(0, len(failReports), 1):
    currentReport = failReports[i].split()
    for j in range(0, len(currentReport), 1):
        safe = True
        levels = []
        for k in range(0, len(currentReport), 1):
            if j != k:
                levels.append(currentReport[k])
        for k in range(0, (len(levels)-1), 1):
            if int(levels[0]) < int(levels[1]) and not (-3 <= int(levels[k]) - int(levels[k + 1]) <= -1):
                safe = False
                break
            elif int(levels[0]) > int(levels[1]) and not (1 <= int(levels[k]) - int(levels[k + 1]) <= 3):
                safe = False
                break
            elif int(levels[0]) == int(levels[1]):
                safe = False
                break
        if safe:
            count += 1
            break
        del levels
    del currentReport

print(count)