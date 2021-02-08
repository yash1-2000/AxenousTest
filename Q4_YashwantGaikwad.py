def printDivisors(n) : 
    i = 1
    sumOfDivisors = 0
    noOfDivisors = 0
    while i <= n : 
        if (n % i == 0) : 
            noOfDivisors = noOfDivisors + 1
            sumOfDivisors = sumOfDivisors + i 
        i = i + 1
    return {'sum': sumOfDivisors, 'divisors': noOfDivisors}

num = int(input("Enter number :"))
answer = printDivisors(num)
print('sum of divisors is',answer['sum'])
print('no of divisors are',answer['divisors'])