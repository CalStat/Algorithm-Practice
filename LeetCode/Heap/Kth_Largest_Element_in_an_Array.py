# 문제명: Kth Largest Element in an Array
# 링크: https://leetcode.com/problems/kth-largest-element-in-an-array/?envType=problem-list-v2&envId=heap-priority-queue
# 작성일: 2026-02-19
# 알고리즘: Heap
# 시간복잡도: O(N)
import heapq as hq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hq.heapify(nums)
        while len(nums) > k :
            hq.heappop(nums)
        return(nums[0])