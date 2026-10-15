class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = int(len(nums)/2)
        for i in range(l, len(nums) - 1):
            if nums[i] == target:
                return i
            elif nums[i] > target:
                i -= 1
            else:
                i += 1

        for i, x in enumerate(nums):
            if x == target:
                return i
        
        return -1