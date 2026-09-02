import re
class Solution:
    def isPalindrome(self, s: str) -> bool:

        res_string = ""

        for i in s:
            if i.isalpha():
                res_string += i.lower()

            if i .isdigit():
                res_string += i
        
        return res_string == res_string[::-1]
        
        
        
        

        