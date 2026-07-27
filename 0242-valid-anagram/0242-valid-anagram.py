class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        new_dict = {}

        for i in s:
            if i in new_dict:
                new_dict[i] += 1
            else:
                new_dict[i] = 1
        
        for j in t:
            if j in new_dict:
                new_dict[j] -= 1
            else:
                print(new_dict)
                return False
        
        for k in new_dict:
            if new_dict[k] != 0:
                return False
        return True

        

