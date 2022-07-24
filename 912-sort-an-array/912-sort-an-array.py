class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(A, I, J):
            A[J-1], A[(I + J - 1)//2], i = A[(I + J - 1)//2], A[J-1], I
            for j in range(I,J):
                if A[j] < A[J-1]: A[i], A[j], i = A[j], A[i], i + 1
            A[J-1], A[i] = A[i], A[J-1]
            return i
        
        # so we are going to do quick sort for this one
        def quicksort(l, h):
            if l < h - 1:
                correct = partition(nums,l,h)
                quicksort(l, correct)
                quicksort(correct + 1, h)
        quicksort(0, len(nums))
        return nums
            
        
        