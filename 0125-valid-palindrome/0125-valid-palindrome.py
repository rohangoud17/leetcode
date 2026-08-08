import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        res_string = ""

        for i in s:
            if (i.isalnum()):
                res_string += (i.lower())
        
        rev_res = res_string[::-1]

        return res_string == rev_res

        

        