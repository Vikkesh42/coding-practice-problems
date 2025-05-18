#https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1


class Solution:
    def longestSubarray(self, arr, k):
        sum =0
        hash ={0:-1}
        length =0
        
        for i in range(len(arr)):
            sum = sum + arr[i]
            
            if (sum - k) in hash:
                length = max(length, i - hash[sum-k])
            if sum not in hash:
                hash[sum] = i
        return length
            
            