class Solution:
    def isValid(self, s: str) -> bool:
        
        mapping = {'}':'{',']':'[',')':'('}

        stack = []

        if (len(s) %2 != 0 or len(s) < 2):
            return False
        
        for i in s:
            if i in mapping:
                if not stack:
                    return False
                if (mapping[i] == stack[-1]):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return not stack

        

        