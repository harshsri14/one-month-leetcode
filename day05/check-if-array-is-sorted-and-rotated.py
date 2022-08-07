# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

def check(nums) :
    breakPoint = 0
    for i in range(1,len(nums)) :
        if nums[i-1] > nums[i] :
            breakPoint += 1
    
    if breakPoint == 0 : 
        return True
    
    if breakPoint == 1 and nums[0]>=nums[len(nums)-1] :
        return True
    
    return False


nums = [3,4,5,1,2]
print(check(nums))
