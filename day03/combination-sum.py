# https://leetcode.com/problems/combination-sum/

def combinationSum(candidates, target) :
	def getCombs(idx, arr, target, ds, ans) :
		if idx == len(arr) :
			if target == 0 :
				ans.append(ds.copy())
			return

		# picking up case
		if arr[idx] <= target :
			ds.append(arr[idx])
			getCombs(idx, arr, target-arr[idx], ds, ans)
			ds.remove(arr[idx])

		# not picking up
		getCombs(idx+1, arr, target, ds, ans)


	ans, ds = [], []
	getCombs(0, candidates, target, ds, ans)
	return ans



candidates = [2,3,5]
target = 8
print(combinationSum(candidates, target))
