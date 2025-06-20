#https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i=0
        j=1

        while j<len(nums):
            if nums[j]!=0 :
                nums[i],nums[j]=nums[j],nums[i]
                i=i+1
                j=j+1
            else:
                j=j+1
