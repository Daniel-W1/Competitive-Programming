#User function Template for python3

class Solution: 
    def select(self, arr, i):
        for x in range(len(arr)):
            i = arr[x]
            for y in range(x,len(arr)):
                if i>arr[y]:
                    i=arr[y]
            index1 = arr.index(i)
            arr[index1], arr[x] = arr[x], arr[index1]
            return i
                    
                    
        # code here 
    
    def selectionSort(self, alist,n):
        for x in range(n):
            i = arr[x]
            for y in range(x,n):
                if i>arr[y]:
                    i=arr[y]
            temp =arr[x]
            arr[x]=i
            for k in range(x+1,len(arr)):
                if i == arr[k]:
                    arr[k]=temp
                    break
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends