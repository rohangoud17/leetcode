class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1

        while(start <= end):
            midVal = (start + end)//2
            if(nums[midVal] == target):
                return midVal
            elif (nums[midVal] > target):
                end = midVal - 1
            else:
                start = midVal + 1
        
        return -1
            