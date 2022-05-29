def partition (Array, low, up):
    i = low+1
    j = up
    pivot = Array[low]
    while(i<=j):
        while(Array[i]<pivot and i<up):
            i=i+1
        while(Array[j]>pivot):
            j = j-1
        if(i<j):
            Array[i], Array [j]
            i=i+1
            j = j-1
        else:
            i=i+1
    Array[low] = Array[j]
    Array[j] = pivot
    print(Array)
    return j
    Array[j], Array[i]


print(partition([13, 18, 8, 10, 21, 7, 2, 32, 6, 19], 0, 9))