#https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binarysearch(nums,target,leftbias):       
            l=0
            u = len(nums) -1
            i=-1
            while l<=u:
                mid = (l+u)//2
                if target > nums[mid]:
                    l=mid+1
                elif target < nums[mid]:
                    u =mid-1
                else:
                    i=mid
                    if leftbias:
                        u=mid-1
                    else:
                        l=mid+1
            return i
        d = binarysearch(nums,target,True)
        r = binarysearch(nums,target,False)
        return [d,r]
        


        
        