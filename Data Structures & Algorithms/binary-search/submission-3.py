class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = len(nums)
        for i, x in enumerate(nums):
            if x == target:
                return i
        
        return -1