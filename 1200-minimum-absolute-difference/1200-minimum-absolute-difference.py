class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        result=[]
        minDiff=arr[1]-arr[0]
        for i in range (len(arr)-1):
            if arr[i+1]-arr[i]<minDiff:
                minDiff=arr[i+1]-arr[i]
                result = [[arr[i], arr[i+1]]]
            elif arr[i+1]-arr[i]==minDiff:
                result+=[[arr[i],arr[i+1]]]
        return result

