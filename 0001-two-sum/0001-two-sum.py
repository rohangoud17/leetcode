class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        new_list = []
        for i in range(len(nums)):
            complement = target - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == complement:
                    new_list = [i,j]
        return new_list


                

        