class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # heap = []

        # for i in nums:
        #     heapq.heappush(heap,i)
        
        return heapq.nlargest(k, nums)[-1]
        