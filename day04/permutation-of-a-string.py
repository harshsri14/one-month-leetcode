def recurPermute(ds, s, ans, freq) :
	if len(ds) == len(s) :
		ans.append(ds.copy())
		return

	for i in range(len(s)) :
		if not freq[i] :
			ds.append(s[i])
			freq[i] = 1
			recurPermute(ds, s, ans, freq)
			freq[i] = 0
			ds.pop()


def permute(s) :
	ans, ds = [], []
	freq = [0]*len(s)

	for i in range(len(s)) :
		recurPermute(ds,s,ans,freq)
	return ans


s = "Harsh"
s = [1,3,2]
res = permute(s)
print(res, len(res))
