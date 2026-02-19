# 문제명: 타겟넘버(BFS)
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/43165
# 작성일: 2026-02-19
# 알고리즘: BFS
# 시간복잡도: O(2^N)

from collections import deque
def solution(numbers,target) :
    answer = 0
    step = 0
    n = len(numbers)
    loc = deque()
    loc.append([step,0])
    while len(loc) > 0 :
        step,cumsum = loc.popleft()
        if cumsum == target and step == n:
            answer += 1
        if step < n :
            step += 1
            loc.append([step,cumsum + numbers[step-1]])
            loc.append([step,cumsum - numbers[step-1]])
    return(answer)