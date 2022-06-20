class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        
        m = (1,1)
        (i-1,j),(i+1,j) (0,1),(2,1)
        (1,0),(1,2)(i,j-1)(i,j+1)
        """
        z_indexes = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    z_indexes.append((i,j))
        # print(z_indexes)
        for item in z_indexes:
            for i in range(len(matrix)):
                # print(i)
                matrix[i][item[1]] = 0
            # print (matrix)
            for j in range(len(matrix[0])):
                matrix[item[0]][j] = 0
            # print (matrix)

                           
                           
                           
        