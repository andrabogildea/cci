class Solution:
    def maxSubArray(self, nums):
        s, maxS = 0, 0
        for nr in nums:
            s += nr
            if maxS < s:
                maxS = s
            if s < 0:
                s = 0
        return maxS

# class Solution:
#     def maxSubArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if len(nums) == 0:
#             return 0
#         end = self.endIndex(nums)
#         start = self.startIndex(nums)
#         # all nrs are negative
#         if start > end:
#             return max(nums)
#         res = self.sumSequence(nums, start, end)
#         return res

#     def endIndex(self, nums):
#         index = 0
#         maxSum = prev = nums[index]
#         for i in range(1, len(nums)):
#             prev += nums[i]
#             if prev > maxSum:
#                 maxSum = prev
#                 index = i
#         return index

#     def startIndex(self, nums):
#         index = len(nums) - 1
#         maxSum = prev = nums[-1]
#         for i in range(len(nums)-2, -1, -1):
#             prev += nums[i]
#             if prev >= maxSum:
#                 maxSum = prev
#                 index = i
#         return index

#     def sumSequence(self, nums, start, end):
#         s = 0
#         for i in range(start, end+1):
#             s += nums[i]
#             print(nums[i])
#         return s

import pytest
@pytest.mark.parametrize('nums, expected', [
    ([], 0),
    ([-2,1,-3,4,-1,2,1,-5,4], 6),
    ([-5, -2, -3, -4], 0),
    ([-5, -6, -7, -1, -9], 0),
    ([1,2,-1,-2,2,1,-2,1], 3),
    ([0,-3,1,1], 2)
])
def test_sol(nums, expected):
    sol = Solution()
    assert sol.maxSubArray(nums) == expected
