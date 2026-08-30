class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        res = 0

        for num in nums:
            if num - 1 not in numset:
                curr = num 
                longest = 1
                while curr+ 1 in numset:
                      curr+=1
                      longest+=1
                res = max(res, longest)
        return res