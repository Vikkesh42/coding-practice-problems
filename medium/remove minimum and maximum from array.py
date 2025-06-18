#https://leetcode.com/problems/removing-minimum-and-maximum-from-array/


class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        # Step 1: Get indices of min and max
        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))

        # Step 2: Arrange so left is the earlier index, right is the later one
        left = min(min_index, max_index)
        right = max(min_index, max_index)

        # Strategy 1: remove from front
        op1 = right + 1

        # Strategy 2: remove from back
        op2 = n - left

        # Strategy 3: remove one from front, one from back
        op3 = (left + 1) + (n - right)

        # Step 3: Return minimum of the three strategies
        return min(op1, op2, op3)
