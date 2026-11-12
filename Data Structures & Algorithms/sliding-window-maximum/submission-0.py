class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = collections.deque()
        idx = 0
        ans = []
        
        while idx < len(nums):
            
            if queue and idx - queue[0] + 1 > k:
                queue.popleft()
            
            while queue and nums[queue[-1]] < nums[idx]:
                queue.pop()
            
            queue.append(idx)

            if idx+1 >= k:
                ans.append(nums[queue[0]])
            idx += 1
        return ans

            