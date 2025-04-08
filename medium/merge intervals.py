#problem: https://leetcode.com/problems/merge-intervals/
#level:medium

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key= lambda x:x[0])

        arr =[intervals[0]]
        rec_end=0

        for start,end in intervals[1:]:
            rec_end= arr[-1][1] 
            if start<=rec_end:
                arr[-1][1] =max(end,rec_end)
            else:
                arr.append([start,end])
        return arr