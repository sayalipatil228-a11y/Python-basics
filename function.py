def calculateGmean(a, b):
    mean = (a*b)/(a+b)
    return mean

def isGreater(a,b):
    if(a>b):
        print("First no. is greater")
    else:
        print("Second no. is greater or equal")

def isLesser(a, b):
    pass

a = 9   
b = 5
result = calculateGmean(a, b)
print(result)
isGreater(a,b)


c = 2
d = 5
result = calculateGmean(c, d)
print(result)
isGreater(c,d)
