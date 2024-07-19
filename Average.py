# Find the average of set of numbers using Python
# Author: Yaswin Prakash

def Average(*args):
    Sum, Count = 0, 0
    for i in args:
        Sum = Sum + i
        Count += 1
    return Sum/Count

NumList = [x**2 for x in range(100)]
print("Average = ", Average(*NumList))
