# Problem: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Level: Easy


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i,j = 0,1
        k=1
        while j<len(nums):
            if nums[i] != nums[j]:
                i=i+1
                nums[i]=nums[j]
                k=k+1
            j=j+1
        return k