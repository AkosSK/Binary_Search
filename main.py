lowerBound = 0
array=[10,20,30,40,50,60,70,80,90,100]
upperBound = len(array) - 1
item=50
Found = False
while Found == False and lowerBound <= upperBound:
    Midpoint = int(round((lowerBound + (upperBound - lowerBound) / 2),0))
if array(Midpoint) == item:
    Found = True
elif array(Midpoint) < item:
    lowerBound = Midpoint + 1
else:
    upperBound = Midpoint - 1
if Found == True:
    print("Item found at " + Midpoint)