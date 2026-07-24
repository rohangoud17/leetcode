class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        new_dict = {}
        new_list = []

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in new_dict:
                new_list = [new_dict[complement], i]
            else:
                new_dict[nums[i]] = i

        return new_list
        
        

 

                

        