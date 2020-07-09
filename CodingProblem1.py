#steps problem
'''Given n steps, find the total number of way to climb the steps if multiple steps can be climbed at once'''

def numWays(n, steps, way):
    if(n == 0):
        return 1
    if(n < 0):
        return 0
    for num in steps:
        way += numWays(n-num, steps, 0)
    return way

print("Number of steps?: ", end='')
n = int(input())

#number of steps that can be taken
steps = [1, 3, 5]

print("Number of ways: ", numWays(n, steps, 0))