class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for index1, x in enumerate(nums):
            for index2, y in enumerate(nums):
                if index1 == index2:
                    continue
                elif x == y and abs(index1 - index2) <= k:
                    return True
                
            
        return False