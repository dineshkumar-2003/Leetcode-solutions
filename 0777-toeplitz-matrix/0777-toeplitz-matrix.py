class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        n=len(matrix)
        m=len(matrix[0])
        if m==0 or m==1:
            return True
        for i in range(n-1):
            for j in range(m-1):
                if matrix[i][j]!=matrix[i+1][j+1]:
                    return False
        return True
        