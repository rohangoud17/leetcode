class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if (len(nums) == 1):
            return nums[0]
        max_no = float('-inf')



        sub_sum = 0

        for i in nums:
            if (sub_sum >= 0):
                sub_sum +=i
            else:
                sub_sum = i
            if (sub_sum > max_no):
                max_no = sub_sum
        
        return max_no
 

            
            
        