def writeFibonacciNumbers(x):
    if x==1:
        return 0
    elif x==2:
        return 1
    else:
        return writeFibonacciNumbers(x-1)+writeFibonacciNumbers(x-2)

findingLine=input("Enter a number: ")
findingLine=int(findingLine)

donut=writeFibonacciNumbers(findingLine)
print(donut)