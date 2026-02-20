# 문제명: 행렬 테두리 회전하기
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/77485?language=python3
# 작성일: 2026-02-20
# 알고리즘: 단순 구현, 시뮬레이션
# 시간복잡도: -

def solution(rows, columns, queries):
    answer = []
    matrix = [[i*columns + j + 1 for j in range(columns)] for i in range(rows)]
    
    for r1,c1,r2,c2 in queries :
        r1,c1,r2,c2 = r1-1,c1-1,r2-1,c2-1
        
        temp = matrix[r1][c2]
        min_val = temp
        for i in range(c2,c1,-1) :
            min_val = min(matrix[r1][i-1],min_val)
            matrix[r1][i] = matrix[r1][i-1]
        
        for i in range(r1,r2) :
            min_val = min(min_val,matrix[i+1][c1])
            matrix[i][c1] = matrix[i+1][c1]
        
        for i in range(c1,c2) :
            min_val = min(min_val,matrix[r2][i+1])
            matrix[r2][i] = matrix[r2][i+1]
            
        for i in range(r2,r1,-1) :
            min_val = min(min_val, matrix[i][c2])
            matrix[i][c2] = matrix[i-1][c2]
            
        matrix[r1+1][c2] = temp
        answer.append(min_val)
    return answer