#https://leetcode.com/problems/binary-search/
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if len(nums) ==1:
            if target == nums[0]:
                return 0
            
        l=0
        u=len(nums)-1

        while l<=u:
            mid =(l+u)//2

            if target == nums[mid]:
                return mid
            else:
                if nums[mid] > target:
                    u=mid-1
                elif nums[mid]<target:
                    l=mid+1
        
        return -1



        