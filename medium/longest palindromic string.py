#https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def find_palindrome(left,right):
            while left >=0 and right <len(s) and s[left]==s[right]:
                left=left-1
                right=right+1
            return s[left+1:right]
        
        long=""

        for i in range(len(s)):
            odd = find_palindrome(i,i)
            even = find_palindrome(i,i+1)
        
            if len(odd) > len(long):
                long=odd
            if len(even) > len(long):
                long = even
        
        return long
