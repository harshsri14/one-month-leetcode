# https://leetcode.com/problems/rotate-image/

def rotate(matrix) :
    """
    Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)
    
    for i in range(n) :
        for j in range(i+1, n) :
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
    for row in matrix :
        row.reverse()



'''
# The above approach is for the leetcode problem only.
# As, it rotate matrix in 90* clock-wise

# To, rotate a matrix in 90* anti-clock-wise this approach is preferred


def transpose(matrix) :
    return list(map(list, zip(*matrix)))


def clockwiseRotate(matrix) :
    matrix = transpose(matrix)

    for i in matrix :
        i.reverse()

    return matrix


def antiClockwiseRotate(matrix) :
    matrix = transpose(matrix)
    
    column = 0
    while column<len(matrix[0]) :
        i = 0
        j = len(matrix)-1

        while i<j :
            matrix[i][column], matrix[j][column] = matrix[j][column], matrix[i][column]
            i += 1
            j -= 1
        column += 1

    return matrix

'''

matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotate(matrix)
print(matrix)
