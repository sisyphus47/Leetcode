class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [x**2 for x in nums]
        return sorted(result)
