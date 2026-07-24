class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        my_dict = defaultdict(list)

        for i in strs:
            count = [0] * 26 #this has 26 empty spots showing each alphabet 

            for j in i:
                count[ord(j) - ord('a')] += 1 #Corresponding index of the alphabet is added
        
            my_dict[tuple(count)].append(i)

        return list(my_dict.values())

        