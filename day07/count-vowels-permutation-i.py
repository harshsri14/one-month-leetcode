# https://leetcode.com/problems/count-vowels-permutation

MOD = 10**9+7

def helper(remainingChar, prevChar, mpp) :
	if remainingChar == 0:
		return 1

	key = str(remainingChar) + prevChar

	if key in mpp :
		return mpp[key]

	if prevChar == 'a' :
		total = helper(remainingChar-1, 'e', mpp)%MOD
	elif prevChar == 'e' :
		total = (helper(remainingChar-1, 'a', mpp) + helper(remainingChar-1, 'i', mpp))%MOD
	elif prevChar == 'i' :
		total = (helper(remainingChar-1, 'a', mpp) + helper(remainingChar-1, 'e', mpp) + 
			helper(remainingChar-1, 'o', mpp) + helper(remainingChar-1, 'u', mpp))%MOD
	elif prevChar == 'o' :
		total = (helper(remainingChar-1, 'i', mpp)+helper(remainingChar-1, 'u', mpp))%MOD
	else :
		total = helper(remainingChar-1, 'a', mpp)%MOD

	mpp[key] = total

	return total


def countVowelPermutation(n) :
	charSet = ['a','e','i','o','u']
	mpp = {}
	total = 0
	for c in charSet :
		total = (total + helper(n-1, c, mpp))%MOD

	return total


n = 144
print(countVowelPermutation(n))
