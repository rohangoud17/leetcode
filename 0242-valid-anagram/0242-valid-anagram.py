class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if (len(s) != len(t)):
            return False
        my_dict = {}
        for i in s:
            if i in my_dict:
                my_dict[i] += 1
            else:
                my_dict[i] = 1
        
        for j in t:
            if j in my_dict:
                my_dict[j] -= 1
        
        for i in my_dict:
            if (my_dict[i] != 0):
                return False
        
        return True

