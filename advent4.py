file1 = open("Input.txt", "r")
lines = file1.readlines()
file1.close()
count = 0

for i in range(0, len(lines), 1):
    for j in range (0, len(lines[i]), 1):
        if (lines[i])[j] == "X":
            try:
                if (lines[i])[j+1] == "M":      #right
                    try:
                        if (lines[i])[j+2] == "A":
                            try:
                                if (lines[i])[j+3] == "S":
                                    count += 1
                            except:
                                pass
                    except:
                        pass
            except:
                pass
            if j>=3:
                try:
                    if (lines[i])[j-1] == "M":    #left
                        try:
                            if (lines[i])[j-2] == "A":
                                try:
                                    if (lines[i])[j-3] == "S":
                                        count += 1
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass
            try:
                if (lines[i+1])[j] == "M":    #up
                    try:
                        if (lines[i+2])[j] == "A":
                            try:
                                if (lines[i+3])[j] == "S":
                                    count += 1
                            except:
                                pass
                    except:
                        pass
            except:
                pass
            if i>=3:
                try:
                    if (lines[i-1])[j] == "M":#down
                        try:
                            if (lines[i-2])[j] == "A":
                                try:
                                    if (lines[i-3])[j] == "S":
                                        count += 1
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass
            if j>=3:
                try:
                    if (lines[i+1])[j-1] == "M":      #up/left
                        try:
                            if (lines[i+2])[j-2] == "A":
                                try:
                                    if (lines[i+3])[j-3] == "S":
                                        count += 1
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass
            if i>=3 and j>=3:
                try:
                    if (lines[i-1])[j-1] == "M":    #down/left
                        try:
                            if (lines[i-2])[j-2] == "A":
                                try:
                                    if (lines[i-3])[j-3] == "S":
                                        count += 1
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass
            try:
                if (lines[i+1])[j+1] == "M":    #up/right
                    try:
                        if (lines[i+2])[j+2] == "A":
                            try:
                                if (lines[i+3])[j+3] == "S":
                                    count += 1
                            except:
                                pass
                    except:
                        pass
            except:
                pass
            if i>=3:
                try:
                    if (lines[i-1])[j+1] == "M":#down/right
                        try:
                            if (lines[i-2])[j+2] == "A":
                                try:
                                    if (lines[i-3])[j+3] == "S":
                                        count += 1
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass


print(count)