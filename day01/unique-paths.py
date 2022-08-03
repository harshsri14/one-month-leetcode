# https://leetcode.com/problems/unique-paths

def getPath(i,j,m,n,dp) :
	if i==m-1 and j==n-1 :
		return 1

	if i>=m or j>=n:
		return 0

	if dp[i][j] != -1 :
		return dp[i][j]

	dp[i][j] = getPath(i+1, j, m, n, dp) + getPath(i, j+1, m, n, dp)

	return dp[i][j]



m = 3
n = 2
dp = [[-1 for i in range(n)]for j in range(m)]
print(getPath(0,0,m,n,dp))
