class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        my_dict = defaultdict(list) #this hashmap maps the count directly to the array of anagrams

        for i in strs:
            count = [0] * 26 # for 26 alphabets

            for j in i: # the letters in the string
                count[ord(j) - ord('a')] += 1

            my_dict[tuple(count)].append(i)
        
        return list(my_dict.values())
                 


        