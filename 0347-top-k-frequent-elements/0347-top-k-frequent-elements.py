class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        my_dict = {}

        for i in nums:
            if i in my_dict:
                my_dict[i] += 1
            else:
                my_dict[i] = 1

        result = []

        for j in range(k):
            highest_key = max(my_dict, key = my_dict.get)
            result.append(highest_key)
            my_dict.pop(highest_key)

        return result

        