arrayOfNo = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
positionArray = []
numberArray = []

for i in range(0, len(arrayOfNo)):
    if(arrayOfNo[i] % 2 == 0):
        positionArray.append(i)
        numberArray.append(arrayOfNo[i])

print("folling are the positions of no divisible by 2",positionArray)
print("folling are numbers divisible by 2",numberArray)