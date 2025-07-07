class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Index to place the next valid element
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        print(nums)
        return k
