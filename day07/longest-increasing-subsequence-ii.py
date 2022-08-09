# https://leetcode.com/problems/longest-increasing-subsequence/
# bisect_left: https://stackoverflow.com/questions/37873954/what-are-pythons-equivalents-of-stdlower-bound-and-stdupper-bound-c-algor

from bisect import bisect_left

def lengthOfLIS(nums) :
    temp = [nums[0]]
    l = 1
    
    for i in range(1, len(nums)) :
        if nums[i] > temp[-1] :
            temp.append(nums[i])
            l += 1
        else :
            idx = bisect_left(temp, nums[i])
            temp[idx] = nums[i]
        
    return l


nums = [10,9,2,5,3,7,101,18]
print(lengthOfLIS(nums))
