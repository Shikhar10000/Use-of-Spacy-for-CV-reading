with open("traindata.json" , "r") as f:
    for line in f:
        cleanedLine = line.strip()
        if cleanedLine: # is not empty
            print(cleanedLine)