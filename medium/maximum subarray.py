#https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largesum = float("-inf")
        sum =0
        
        for i in nums:
            sum = sum + i
            if sum<i:
                sum=i
            if sum>largesum:
                largesum=sum
        
        return largesum