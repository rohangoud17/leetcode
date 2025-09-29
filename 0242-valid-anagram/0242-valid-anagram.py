class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        
        
        counter = {}

        for i in s:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1


        for j in t:
            if j in counter and counter[j] > 0:
                counter[j] -= 1
            else:
                return False

        return True

    
            



        