# https://leetcode.com/problems/combination-sum-iv/

def combinationSum4(nums, target) :
    def getCombs(nums, target, dp) :
        if target<0 :
            return 0
        if target == 0 :
            return 1
        if dp[target] != -1 :
            return dp[target]
        
        ans = 0
        for i in range(len(nums)) :
            ans += getCombs(nums, target-nums[i], dp)
        
        dp[target] = ans
        return dp[target]
    
    dp = [-1 for i in range(target+1)]
    return getCombs(nums, target, dp)


nums = [1,2,3]
target = 4
print(combinationSum4(nums, target))
