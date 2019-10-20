import math
import numpy as np
# Simple array sum


def simpleArraySum(n, ar):

    if n > 0:
        sum = 0
        for value in ar:
            if value > 1000:
                return('Violation of constraints, element too large')
                break
            sum = sum + value
        return(sum)
    else:
        return('Violation of constraints, array length error')


print(simpleArraySum(3, [1, 2, 3]))

# Compare the triplets


def compreTriplets(a, b):
    lengthA = len(a)
    lengthB = len(b)
    if lengthA != lengthB or lengthA != 3:
        return('Error')
    else:
        result = [0, 0]
        c = [a, b]
        for i in range(lengthA):
            if c[0][i] > 100 or c[1][i] > 100:
                return('Error')
                break
            elif c[0][i] == c[1][i]:
                result = result
            elif c[0][i] > c[1][i]:
                result[0] = result[0] + 1
            else:
                result[1] = result[1] + 1
        return(result)


print(compreTriplets([101, 2, 47], [27, 6, 47]))

# A very big sum


def aVeryBigSum(ar):
    sum = 0
    for i in range(len(ar)):
        if ar[i] > 10 ** 10 or ar[i] < 0 or len(ar) > 10 or len(ar) < 0:
            return('Error')
            break
        else:
            sum = sum + ar[i]
    return(sum)


print(aVeryBigSum([1, 2, 3]))

# Matching socks
print('BREAK')


def sockMerchant(n, ar):
    if n < 1 or n > 100:
        return('Error')
    ar.sort()
    distinct = set(ar)
    sum = 0
    for i in distinct:
        if i > 100 or i < 1:
            return('Error')
            break
        else:
            sum = sum + math.floor(ar.count(i)/2)
    return(sum)


print(sockMerchant(12, [1, 1, 1, 1, 2, 3, 2, 4, 4, 4, 4, 4, 4, 4]))

# Left rotation function


def rotLeft(a, d):
    if len(a) < 1 or len(a) > 10 ** 5 or d < 1 or d > len(a):
        return('Error')
    else:
        for i in range(0, d):
            if a[i] > 10 ** 6 or a[i] < 1:
                return('Error')
            else:
                a.append(a[0])
                a.remove(a[0])
        return(a)


print(rotLeft([1, 2, 3, 4, 5], 3))
