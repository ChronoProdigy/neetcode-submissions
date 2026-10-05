class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        answer = nums.copy()
        for x in nums:
            answer.append(x)
        return answer