class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zero_cnt = arr.count(0)
        n = len(arr)
        
        for idx in range(n-1, -1, -1):
            if arr[idx] == 0:
                zero_cnt -= 1
            
            new_idx = idx + zero_cnt
            if new_idx < n:
                arr[new_idx] = arr[idx]
            
            if arr[idx] == 0 and new_idx + 1 < n:
                arr[new_idx + 1] = arr[idx]
        
                