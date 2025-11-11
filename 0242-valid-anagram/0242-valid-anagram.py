class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if(len(s) != len(t)):
            return False
        dic = {}
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1

        
        for j in t:
            if j in dic and dic[j] > 0:
                dic[j] -= 1
            else:
                return False


        return True