# def divisorSum( n ):
#     sum = 0
#     for i in range(1, n):
#         # Find all divisors of i
#         # and add them
#         j = 1
#         while j * j <= i:
#             if i % j == 0:
#                 if i / j == j:
#                     sum += j
#                 else:
#                     sum += j + i / j
#             j = j + 1
#     return int(sum)

# def divisorSum( n ):
#     sum = 0
#     for i in range(1, n):
#         # Find all divisors of i
#         # and add them
#        if(n % i == 0):
#         #    noOfDivisors = noOfDivisors + 1
#            sum = sum + i
#     return int(sum)
 
# # Driver code
# num = int(input("Enter number :"))
# print( divisorSum(num))

def printDivisors(n) : 
    i = 1
    sumOfDivisors = 0
    noOfDivisors = 0
    while i <= n : 
        if (n % i==0) : 
            print(i)
            noOfDivisors = noOfDivisors + 1
            sumOfDivisors = sumOfDivisors + i 
        i = i + 1
    return {'sum_': sumOfDivisors, 'divisors': noOfDivisors}
 
answer = printDivisors(25)
print('sum of divisors is',answer[sum_])
print('no of divisors are',answer[divisors])