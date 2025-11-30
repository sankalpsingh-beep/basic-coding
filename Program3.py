def findSeries(x):
    result = [str(2*i - 1) for i in range(1, x + 1)]
    outputList = []
    for num in range(len(result)):
        if((num+1) % 2 == 0):
            outputList.append(outputList[len(outputList)-1])
        else:    
            output = ",".join(result[:num+1])
            outputList.append(output)
    for index in range(len(outputList)):
        print(f"input a = {index+1}, then output: {outputList[index]}")

x = int(input("Enter the value of x: "))
findSeries(x)
