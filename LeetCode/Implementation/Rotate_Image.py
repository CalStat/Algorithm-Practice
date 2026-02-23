# 문제명: Rotate Image
# 링크: https://leetcode.com/problems/rotate-image/description/
# 작성일: 2026-02-23
# 알고리즘: Implementation
# 시간복잡도: O(N^2)

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # transpose 
        for i in range(n) :
            for j in range(i) :
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        # flip
        for i in range(n) :
            for j in range(int(n/2)) :
                temp = matrix[i][n-1-j]
                matrix[i][n-1-j] = matrix[i][j]
                matrix[i][j] = temp