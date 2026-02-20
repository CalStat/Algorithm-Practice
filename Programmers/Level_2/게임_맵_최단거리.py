# 문제명: 게임 맵 최단거리
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/1844
# 작성일: 2026-02-20
# 알고리즘: BFS
# 시간복잡도: O(NM) <- 완전탐색이므로

from collections import deque

def is_valid_yx (y,x,leny,lenx,maps) :
    return 0<=y<leny and 0<=x<lenx and maps[y][x] == 1

def solution(maps):
    leny,lenx = len(maps),len(maps[0])
    if maps[leny-1][lenx-1] == 0 :
        return -1
    dy = [1,0,-1,0]
    dx = [0,1,0,-1]
    dq = deque()
    dq.append((0,0,1))
    maps[0][0] = 0
    while dq:
        y,x,step = dq.popleft()
        if y == leny-1 and x == lenx-1 :
            return step
        for i in range(4) :
            ny = y + dy[i]
            nx = x + dx[i]
            if is_valid_yx(ny,nx,leny,lenx,maps) :
                maps[ny][nx] = 0
                dq.append((ny,nx,step+1))
    return -1