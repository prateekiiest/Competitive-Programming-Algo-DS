# Problem Statement:https://www.interviewbit.com/courses/1/topics/4/problems/matrix-median

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def findMedian(self, A):
        l = []
        rows  = len(A)
        cols = len(A[0])
        for i in range(rows):
            for j in range(cols):
                l.append(A[i][j])
                
    
        p = sorted(l)
        mid = (len(p)/2)
        return p[mid]
