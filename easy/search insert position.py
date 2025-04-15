#https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=0
        u=len(nums)-1

        while l<=u:
            mid=(l+u)//2
            if target==nums[mid]:
                return mid
            else:
                if target>nums[mid]:
                    l=mid+1
                elif target<nums[mid]:
                    u=mid-1
        return l


