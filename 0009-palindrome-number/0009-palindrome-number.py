class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        digit_list =[digit for digit in str(x)]
        if(digit_list == digit_list[::-1]):
            return True
        else:
            return False