#https://leetcode.com/problems/maximum-product-subarray/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curmax = curmin = res = nums[0]

        for i in nums[1:]:

            if i < 0:
                curmax,curmin = curmin,curmax

            curmax = max(i,curmax*i) 
            curmin = min(i,curmin*i)
            res = max(curmax,res)

        return res      