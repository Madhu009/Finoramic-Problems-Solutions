class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        '''import math
        result1=math.pow(x,n)
        result2=result1%d

        return int(result2)'''

        '''r1=x**n
        r2=r1%d

        return r2''' # getting timed out

        return pow(x, n, d) #better and faster is python built in function
