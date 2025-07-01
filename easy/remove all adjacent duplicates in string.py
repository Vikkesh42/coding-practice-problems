#https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
class Solution:
    def removeDuplicates(self, s: str) -> str:
        temp=[]
        for ch in s:
            if temp and temp[-1]==ch:
                    temp.pop()
            else:
                temp.append(ch)  
        return ''.join(temp)              