# https://leetcode.com/problems/longest-increasing-subsequence/

def lengthOfLIS(nums) :
	def f(idx, prev_idx, nums) :
		if idx == len(nums) :
			return 0

		len_ = 0 + f(idx+1, prev_idx, nums)

		if prev_idx == -1 or nums[idx] > nums[prev_idx] :
			len_ = max(len_, 1 + f(idx+1, idx, nums))

		return len_

	return f(0, -1, nums)


nums = [10,9,2,5,3,7,101,18]
print(lengthOfLIS(nums))
