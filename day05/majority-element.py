# https://leetcode.com/problems/majority-element

def majorityElement(nums) :
    '''
    # approach-1  :: O(n^2) & O(1)

    threshold = len(nums)//2 if len(nums)%2==0 else (len(nums)+1)//2
    
    for i in nums :
        count = 0
        for j in nums :
            if i==j :
                count += 1

            if count >= threshold :
                return i
    '''

    '''
    # approach-2  :: O(nlogn) & O(1)
    
    nums.sort()
    return nums[len(nums)//2]

    '''    

    '''
    # approach-3  :: O(n) and O(n)

    hMap = {}
    threshold = len(nums)//2 if len(nums)%2==0 else (len(nums)+1)//2
    
    for n in nums :
        hMap[n] = hMap.get(n, 0)+1
    
    for k,v in hMap.items() :
        if v >= threshold :
            return k
    '''

    
    # approach-4  :: O(n) & O(1)
    # Boyer-Moore Majority Voting Algorithm

    major = nums[0]
    count = 0

    for num in nums :
        if count==0 :
            major = num

        if num == major :
            count += 1
        else :
            count -= 1

    return major


nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))
