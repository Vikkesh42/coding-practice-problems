#https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l=0
        u=len(nums)-1

        while l<=u:

            mid = (l+u)//2

            if nums[mid] == target:
                return mid
            
            else:
                if nums[l]<=nums[mid]:
                    if target > nums[mid] or target < nums[l]:
                        l=mid+1
                    else:
                        u=mid-1
                
                else:
                    if target <nums[mid] or target > nums[u]:
                        u=mid-1
                    else:
                        l=mid+1
        return -1
