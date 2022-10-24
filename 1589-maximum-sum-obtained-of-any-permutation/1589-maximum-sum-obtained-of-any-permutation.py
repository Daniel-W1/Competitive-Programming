class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        '''
        [[0,2], [1,3], [1,1]]
        [1,2,-1,-1,0,-1]
        [1,3,2,1,1,0]
        [2, 10, 5, 4, 3, 1]
        
        17 + 19 + 10
        '''
        nums_size = len(nums)
        query_count = [0]* nums_size
        mod = 10**9 + 7
        
        for start, end in requests:
            query_count[start] += 1
            
            if end + 1 < nums_size:
                query_count[end+1] -= 1
        
        query_count = list(accumulate(query_count))
        nums.sort()
        query_count.sort()
        answer = 0
        
        for idx in range(nums_size):
            answer += ((nums[idx] * query_count[idx]))%mod
            
        # print(query_count)
        return answer % mod