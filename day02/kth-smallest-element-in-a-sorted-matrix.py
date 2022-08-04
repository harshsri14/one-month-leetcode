# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

def kthSmallest(matrix, k) :
    arr = []
    
    for i in range(len(matrix)) :
        for j in range(len(matrix[0])) :
            arr.append(matrix[i][j])
            
    arr.sort()
    
    return arr[k-1]


matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8
print(kthSmallest(matrix, k))
