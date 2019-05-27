# Submission Link : https://leetcode.com/submissions/detail/231268222/

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # create a hash table for all the unique characters against the frequency
        # of each character in the string
        
        uniq_s = set(s)
        has = {}
        for k in uniq_s:
            has[k] = s.count(k)
            
        
        
        le = 0
        odd_great_one = False # if we have odd occurences greater than 1
        one = False # only single occurence of a character
        for k in has:
            if has[k]%2 == 0: # if even occurence of a character
                le += has[k] # increase by that amnt
            elif has[k]%2 != 0 and has[k] >1: # else if odd ocurrence
                le += has[k] -1
                odd_great_one = True # add the extra odd char as the middle elem in palindrome
            
            elif has[k]%2 == 1: # else if single occurence, take it as elem  in the middle of the palindrome
                one = True                
        if odd_great_one == True:
            le += 1
        if one == True and odd_great_one == False:
            le += 1
        return le
