class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def findmaxindex(arr):
            l = 0
            maxele = -1
            for h in range(len(arr)):
                if arr[h] > maxele:
                    l = h
                    maxele = arr[h]
            return l
        def issorted(arr):
            for i in range(len(arr)-1):
                if arr[i+1] - arr[i] < 0:
                    return False
            return True
        endpoint = len(arr)
        output = []
        while not issorted(arr):
            pos = findmaxindex(arr[:endpoint])
            arr = arr[:pos+1][::-1] + arr[pos+1:]
            output.append(pos+1)
            arr = arr[:endpoint][::-1]
            output.append(len(arr))
            endpoint -= 1
        return output
            
                    
            