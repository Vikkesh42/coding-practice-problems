#https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        e_sum = n*(n+1)//2
        a_sum=sum(nums)

        s=e_sum-a_sum
        return s