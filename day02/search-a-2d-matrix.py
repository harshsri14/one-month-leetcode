# https://leetcode.com/problems/search-a-2d-matrix

def searchMatrix(matrix, target) :
	r, c = 0, len(matrix[0])-1

	while r<len(matrix) and c>=0 :
		if matrix[r][c] == target :
			return r,c

		elif matrix[r][c] > target :
			c -= 1

		else :
			r += 1

	return -1



matrix = [[ 1, 3, 5, 7],
		  [10,11,16,20],
		  [23,30,34,60]]

target = 23

print(searchMatrix(matrix, target))
