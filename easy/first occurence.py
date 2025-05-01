#https://www.geeksforgeeks.org/problems/number-of-occurrence2259/1

class Solution:
    def countFreq(self, arr, target):
        #code here
        def bin_search(arr,target,leftbias):
            l=0
            u=len(arr)-1
            i=-1
            while l<=u:
                mid = (l+u)//2
                
                if target > arr[mid]:
                    l=mid+1
                elif target < arr[mid]:
                    u=mid-1
                else:
                    i=mid
                    if leftbias:
                        u = mid-1
                    else:
                        l=mid+1
            return i
        
        s=bin_search(arr,target,True)
        d=bin_search(arr,target,False)
        
        if s==-1:
            return 0
        else:
            return d-s+1
                        
            
        