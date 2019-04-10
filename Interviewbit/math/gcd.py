# Problem : https://www.interviewbit.com/courses/1/topics/3/problems/greatest-common-divisor
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, a, b):
        while b:
            a, b = b, a%b
        return a
