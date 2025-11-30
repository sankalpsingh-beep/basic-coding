def findSeries(x):
    result = [str(2*i - 1) for i in range(1, x + 1)]
    
    for num in range(len(result)):
        output = ",".join(result[:num+1])
        print(f"input a = {num+1}, then output: {output}")

x = int(input("Enter the value of x: "))
findSeries(x)
