#https://www.geeksforgeeks.org/problems/rotation4723/1

#User function Template for python3
class Solution:
    def findKRotation(self, arr):
        # code here
        l=0
        u=len(arr)-1
        
        while l<u:
            
            mid =(l+u)//2
            
            if arr[u] < arr[mid]:
                l=mid+1
            else:
                u=mid
        return l
                