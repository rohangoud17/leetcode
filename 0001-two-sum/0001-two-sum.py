class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        if len(nums) == 2:
            return [0,1]
        for i in range(len(nums)):
            complement = target - nums[i]
            for j in range(i+1,len(nums)):
                if nums[j] == complement:
                    return [i,j]

                

        