class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if (len(s) < 2):
            return False
        
        if (len(s) % 2 != 0):
            return False
        
        my_dict = {')': '(', '}':'{',']':'['}

        stack = []

        for i in s:
            if i in my_dict:
                if not stack:
                    return False
                if (stack[-1] == my_dict[i]):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        
        if  len(stack) == 0:
            return True
        else:
            return False

        
        
        