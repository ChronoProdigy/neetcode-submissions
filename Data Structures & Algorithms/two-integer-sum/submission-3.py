class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for x, y in enumerate(nums):
            diff = target - y
            if diff in seen:
                return [seen[diff], x]
            else:
                seen[y] = x

        