class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0

        for n in nums:
            if n - 1 not in numSet:
                curr = n 
                longest = 1
                while curr + 1 in numSet:
                      curr+=1
                      longest+=1
                res = max(res, longest)
        return res