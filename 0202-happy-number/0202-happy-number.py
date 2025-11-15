class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visit = set()

        while n not in visit:
            visit.add(n)
            n = self.sumOfSquares(n)

            if(n == 1):
                return True
        return False

    def sumOfSquares(self, j):
        output = 0
        tens = j % 10
        tens = tens**2
        output += tens 
        j = j // 10
        return output 


        