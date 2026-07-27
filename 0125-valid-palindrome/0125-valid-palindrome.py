import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        res_string = ""
        for i in s:
            if i.isalpha():
                res_string += i.lower()
            if i.isdigit():
                res_string += i
        
        
        res_rev = res_string[::-1]

        return res_rev == res_string
        



        
        
        