#https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)

        def rev(arr,i,j):
            while i<j:
                arr[i],arr[j] = arr[j],arr[i]
                i=i+1
                j=j-1
        rev(nums,0,len(nums)-1)
        rev(nums,0,k-1)
        rev(nums,k,len(nums)-1)

        return nums




        