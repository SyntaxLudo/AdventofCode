file1 = open("Input.txt", "r")
lines = file1.readlines()
file1.close()
count = 0

for i in range(1, len(lines)-1, 1):
    for j in range (1, len(lines[i])-1, 1):
        if (lines[i])[j] == "A":
            try:
                if (lines[i-1])[j+1] == "M":
                    try:
                        if (lines[i+1])[j+1] == "S":
                            try:
                                if (lines[i+1])[j-1] == "S":
                                    try:
                                        if (lines[i-1])[j-1] == "M":
                                            count += 1
                                    except:
                                        pass
                            except:
                                pass
                    except:
                        pass
            except:
                pass
            try:
                if (lines[i-1])[j+1] == "S":
                    try:
                        if (lines[i+1])[j+1] == "S":
                            try:
                                if (lines[i+1])[j-1] == "M":
                                    try:
                                        if (lines[i-1])[j-1] == "M":
                                            count += 1
                                    except:
                                        pass
                            except:
                                pass
                    except:
                        pass
            except:
                pass
            try:
                if (lines[i-1])[j+1] == "M":
                    try:
                        if (lines[i+1])[j+1] == "M":
                            try:
                                if (lines[i+1])[j-1] == "S":
                                    try:
                                        if (lines[i-1])[j-1] == "S":
                                            count += 1
                                    except:
                                        pass
                            except:
                                pass
                    except:
                        pass
            except:
                pass
            try:
                if (lines[i-1])[j+1] == "S":
                    try:
                        if (lines[i+1])[j+1] == "M":
                            try:
                                if (lines[i+1])[j-1] == "M":
                                    try:
                                        if (lines[i-1])[j-1] == "S":
                                            count += 1
                                    except:
                                        pass
                            except:
                                pass
                    except:
                        pass
            except:
                pass


print(count)