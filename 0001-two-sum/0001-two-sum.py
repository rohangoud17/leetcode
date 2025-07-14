class Solution(object):
    def twoSum(self, nums, target):
        result_list = []
        # for i in nums:
        #     for j in nums[1:]:
        #         if i + j == target:
        #             result_list.append(nums.index(i))
        #             result_list.append(nums.index(j))
        #         continue
        # result_list =  list(set(result_list))

        # return result_list

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if ((nums[i] + nums[j]) == target ):
                    result_list.append(j)
                    result_list.append(i)
                    break
                continue
        # result_list =  list(set(result_list))
        return result_list

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        