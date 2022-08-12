# https://leetcode.com/problems/binary-trees-with-factors/

def numFactoredBinaryTrees(arr) :
    arr.sort()
    mpp = {i:1 for i in arr}
    
    for i in range(1, len(arr)) :
        count = 0
        for j in range(i) :
            if arr[i]%arr[j] == 0 :
                if arr[i]//arr[j] in mpp :
                    count += mpp[arr[j]] * mpp[arr[i]//arr[j]]
        mpp[arr[i]] += count
            
            
    return sum(mpp.values())%(10**9+7)


arr = [2,4,5,10]
print(numFactoredBinaryTrees(arr))
