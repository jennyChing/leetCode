# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"
import heapq
# helper function binary search to find the position of stone to insert new out of water stones
def biSearch(A, a):
    left, right = 0, len(A) - 1
    while right > left:
        mid = (right - left) // 2
        if a > A[mid]:
            print(a, A, A[mid], left, mid, right)
            left = mid + 1
        else:
            print(a, A, left, mid, right)
            right = mid
    return left

def solution(A, D):
    # write your code in Python 2.7
    if D > len(A):
        return 0
    position_lookup = {}
    for i in range(len(A)):
        position_lookup[A[i]] = i
    sortedA = sorted(A)
    stones, isJumped = [len(A)], False
    for a in sortedA:
        if a > 0:
            stones.insert(biSearch(stones, a), position_lookup[a])
            frog_curr = -1
            for s in stones:
                if s - frog_curr > D:
                    isJumped = False
                    break
                isJumped = True
                frog_curr = s
            if isJumped == True:
                return a
    return -1
if __name__ == '__main__':
    res = solution([1, 4, -1, 6], 2)
    print(res)
'''
1. My solution is to loop thourgh the value (time of stone be out of water) in the Array A in increasing order, and check if the frog can jump from position -1 to N (equals to the length of Array A) at each time point. If not, it will check the next smallest time in the Array A. If the frog succeeds. it will return the time and exit the program.

Below is the components of my program:
    (1). Create a hashtable "position_lookup" with a for loop to map the stones' positions and out of water time for later use.
    (2). Keep an array to store all the out of water stones that the frog can jump on to.
    (3). Sort the Array A in increasing order and use a for loop to loop through the sorted array.
    (4). Within the for loop, use binary search to insert the position (check the hashtable "position_lookup") of the new out of water stone that came available at this certain time point in to the stones array. And then loop through the stones to check if the frog can succeed to pass the river with these stones.
    (5). If the frog fails (the next stone to its current position is larger then D), the for loop breaks and go on to check the next time in the Array A.
    (6). If the frog succeeds (all of the next stone to its current position is not larger then D), it returns the current time a.



2. Both of my experience in Google and urAD helped my beheld how the advertising industry is transforming itself to be driven by data rather than guesswork. With every communication with consumers being recorded as data point by companies like LiveRamp, advertisers are capable of optimizing performances based on data analysis. I look forward to work with the talented and young team at LiveRamp in this industry that I truely love!
'''
