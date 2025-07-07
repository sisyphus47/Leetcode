class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0
        for i in range(1, n - 1):
            # Check if current element is a peak
            if arr[i - 1] < arr[i] > arr[i + 1]:
                left = i - 1
                right = i + 1
                # Expand left while strictly increasing
                while left > 0 and arr[left - 1] < arr[left]:
                    left -= 1

                # Expand right while strictly decreasing
                while right < n - 1 and arr[right] > arr[right + 1]:
                    right += 1

                # Update result with the length of current mountain
                res = max(res, right - left + 1)

        return res
