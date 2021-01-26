import random

def qsort_random(array, left=0, right=8):
    global count    
    p = random.choice(array[left:right+1])
    i,j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            count += 1
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
        
    if j > left:
        qsort_random(array, left, j)
    if right > i:
        qsort_random(array, i, right)

count = 0
array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
right = len(array)-1

qsort_random(array)
print(array)
print(count)
