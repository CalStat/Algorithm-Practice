# 문제명: Surrounded regions
# 링크: https://leetcode.com/problems/surrounded-regions/description/
# 작성일: 2026-02-23
# 알고리즘: BFS
# 시간복잡도: O(MN)

from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m,n = len(board),len(board[0])
        
        # BFS 
        dx = [1,0,-1,0]
        dy = [0,1,0,-1]
        visited = deque()
        # finding enterances in boundary
        for i in range(m) :
            if board[i][0] == "O":
                visited.append([i,0])    
                board[i][0] = "V"
            if board[i][n-1] == "O":
                visited.append([i,n-1])
                board[i][n-1] = "V"
        for j in range(1,n-1) :
            if board[0][j] == "O":
                visited.append([0,j])    
                board[0][j] = "V"
            if board[m-1][j] == "O":
                visited.append([m-1,j])
                board[m-1][j] = "V"
        # searching
        while visited :
            y,x = visited.popleft()
            for i in range(4) :
                ny,nx = y+dy[i],x+dx[i]
                if 0<=ny<m and 0<=nx<n and board[ny][nx] == "O" :
                    visited.append([ny,nx])
                    board[ny][nx] = "V"
        #replacing
        for i in range(m) :
            for j in range(n) :
                if board[i][j] == "V" :
                    board[i][j] = "O"
                else :
                    board[i][j] = "X"