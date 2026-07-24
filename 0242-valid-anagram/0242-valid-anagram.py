class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t) :
            return False
        
        my_dict = {}

        for i in s:
            if i in my_dict:
                my_dict[i] += 1
            else:
                my_dict[i] = 1
        
        for j in t:
            if j not in my_dict:
                return False
            else:
                my_dict[j] -= 1
        
        for k in my_dict:
            if my_dict[k] > 0:
                return False

        return True



    
            



        