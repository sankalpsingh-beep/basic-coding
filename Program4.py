def createDic(numsList):
    outDict = {k: 0 for k in range(1, 10)}
    for key in outDict:
        count = 0
        for num in numsList:
            if (num % key == 0):
                count += 1
        outDict[key] = count
    return outDict

numsList = list(map(int, input("Enter integers (comma-separated): ").split(",")))
print(createDic(numsList))
