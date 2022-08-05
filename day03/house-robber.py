# https://leetcode.com/problems/house-robber

def rob(nums) :
    dp = [[0,0] for i in range(len(nums)+1)]
    
    for i in range(1,len(nums)+1) :
        dp[i][0] = dp[i-1][1] + nums[i-1]
        dp[i][1] = max(dp[i-1])
    
    return max(dp[-1])


nums = [2,7,9,3,1]
print(rob(nums))
