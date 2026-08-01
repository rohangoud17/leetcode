class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        heap = []

        for n in nums:
            heapq.heappush(heap, n)
        
        return heapq.nlargest(k, heap)[-1]
        

        




        