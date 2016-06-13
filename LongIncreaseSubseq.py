'''

Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4.
'''

def lengthOfLIS(seq):
    if not seq: # seq is empty
        return seq
    M = [None] * len(seq) # the list of indexes that are increasing (no numbers on the right is smaller than it)
    P = [None] * len(seq) # list to build the result at the end: records which is the previous element of the current longest subsequence

# initiate the LIS with the first element
    L = 1 # the updated length of longest subseq over the loop
    M[0] = 0
# start looping from the second element
    for i in range(1, len(seq)):
# for each index, init the lower and upper value (upper is the max of length of LTS and the value j (set to either lower or upper)
        lower, upper = 0, L
# Case 1: the current i is increased from last number (compare to previous number)
        if seq[M[upper - 1]] < seq[i]:
            j = upper # current element is part of the LIS, so update upper and length L
            #print("Case1", M, upper, i)
# Case 2: the current i is decreased from last number, so drop the previous one/ones (check with binary search) and update the M and P
        else: # the binary search loop to find j that seq[M[j]] < seq[i]
            while upper - lower > 1:

### what is the lower/upper and mid here? find the smallest value?

                #print(j, seq[M[upper - 1]], seq[i])
                mid = (upper + lower) // 2
                if seq[M[mid - 1]] < seq[i]:
                    lower = mid
                    print(lower, mid, upper)
                else:
                    upper = mid
                    print(lower, mid, upper)
                #print("Case 2", M, i, upper, lower)
            j = lower # set the default value to 0, then record the smallest on the left
            #print("Case2", M, i, upper, lower)
# update P and M
        P[i] = M[j - 1]
# j is the pointer of current updated index in M
        if j == L or seq[i] < seq[M[j]]:
            M[j] = i
# update the length of LTS:
            L = max(L, j + 1)
        print('i', i, 'L:', L, 'M:', M, 'lower/uppder', lower, upper, 'j:', j)
    result = []
    pos = M[L - 1]
    for _ in range(L):
        result.append(seq[pos])
# the index in P will point to the next element in the LIS
        pos = P[pos]
    return result[::-1]

if __name__ == '__main__':
    seq = [10, 9, 2, 5, 3, 7, 101, 18]
    result = lengthOfLIS(seq)
    print(result)
