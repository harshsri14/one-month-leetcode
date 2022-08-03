# https://leetcode.com/problems/pascals-triangle

def getNCR(n,r) :
	res = 1

	for i in range(1, r+1) :
		res = res * (n-r+i)/i

	return int(res)


def pascalTriangle(n) :
	result = [[1]]
	if n==1 :
		return result

	elif n==2 :
		result.append([1,1])
		return result

	else :
		result.append([1,1])

		for i in range(2, n) :
			row = [1]

			for j in range(1, i) :
				value = getNCR(i,j)
				row.append(value)

			row.append(1)
			result.append(row)

		return result

n = 7
print(pascalTriangle(n))
