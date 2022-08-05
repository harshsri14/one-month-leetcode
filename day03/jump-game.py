# https://leetcode.com/problems/jump-game

def canJump(nums) :
    if len(nums)==1 : return True
    s = 0
    e = 0
    while s<=e :
        new = s + nums[s]
        if new>e : 
            e = new
            if e>=len(nums)-1 :
                return True
        s += 1
    
    return False


nums = [2,3,1,1,4]
print(canJump(nums))
