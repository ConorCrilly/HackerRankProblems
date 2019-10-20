# bubble sort implementation
# This is a test change


def countSwaps(a):
    numSwaps = 0
    while(a != sorted(a)):
        for i in range(len(a) - 1):
            if a[i] > a[i+1]:
                numSwaps += 1
                a[i], a[i+1] = a[i + 1], a[i]
    print("Array is sorted in {} swaps.".format(numSwaps))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[-1]))
    return(numSwaps, a)


countSwaps([6, 4, 1])

print('This is a change!')
