class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k = k % n
        l=nums[0:n-k]
        print(len(l))
        r=nums[n-k:n]
        print(len(r))
        a=0
        for i in range(0,k):
            nums[i]=r[i]
        for i in range(k,n):
            nums[i]=l[a]
            a+=1


            
        