def find(array, element):
    for i, a in enumerate(array):
        if a == element:
            return i
    return False


def count(array, element):
    count = 0 
    for i in array:
        if i == element:
            count += 1
    return count




array = list(map(int, input().split()))
element = int(input())

print(find(array, element))
print(count(array, element))