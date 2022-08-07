# https://leetcode.com/problems/transpose-matrix/

# approach-1  :: for M*M matrix i.e. Square matrix only
# O(M^2) & O(1)
def transposeMM(matrix) :
    for i in range(len(matrix)) :
        for j in range(i+1, len(matrix[0])) :
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    return matrix


# approach-2  :: for M*N matrix 
# O(m*n) & O(m*n)
def transposeMN(matrix) :
    result = [[0 for i in range(len(matrix))]for j in range(len(matrix[0]))]

    for i in range(len(matrix)) :
        for j in range(len(matrix[0])) :
            result[j][i] = matrix[i][j]

    return result


# approach-3  :: for M*N matrix
# O(m*n) & O(m*n)
def transposeUsingZip(matrix) :
    result = []
    for row in zip(*matrix) :
        result.append(list(row))
    return result

def transposeZipOther(matrix) :
    return list(map(list, zip(*matrix)))



matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]


print(transposeUsingZip(matrix))
#print(transposeMM(matrix))
#print(transposeMN(matrix))
