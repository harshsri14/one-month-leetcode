# https://leetcode.com/problems/count-vowels-permutation

def countVowelPermutation(n) :
    dp = [[], [1,1,1,1,1]]
    a, e, i, o, u = 0, 1, 2, 3, 4
    mod = 10**9 + 7

    for j in range(2, n+1) :
        dp.append([0,0,0,0,0])
        
        dp[j][a] = (dp[j-1][e] + dp[j-1][i] + dp[j-1][u]) % mod
        dp[j][e] = (dp[j-1][a] + dp[j-1][i]) % mod
        dp[j][i] = (dp[j-1][e] + dp[j-1][o]) % mod
        dp[j][o] = (dp[j-1][i])
        dp[j][u] = (dp[j-1][i] + dp[j-1][o]) % mod

    return sum(dp[n]) % mod


n = 2
print(countVowelPermutation(n))
