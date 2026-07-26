class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        new_dict = {}
        complement = 0
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if (complement in new_dict):
                return [i, new_dict[complement]]
            new_dict[nums[i]] = i 
        
        return -1
        

        

 

                

        