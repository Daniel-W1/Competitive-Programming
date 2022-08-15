class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # stack monoStack increasing
        # 1, 2, 3
        # 1, 5, 0
        # [2,1,5,0,6]
        # 0, 6
        # 1,5,6
        
        #[2,1,5,0,4,6]
        # 2, 5, 6
        # n^3
        # for every n we are looking another partners in the whole array
        # n^2
        # [2,1,5,0,4,6]
        # finding an element that has next greater and previous smaller
        
        
        # step1 check if their is a next greater element
        check1 = [False]*len(nums)
        stack = []
        for idx,number in enumerate(nums):
            while stack and number > stack[-1][1]:
                index, value = stack.pop()
                check1[index] = True
            stack.append((idx, number))

        check2 = [False]*len(nums)
        stack = []
        for idx in range(len(nums)-1,-1,-1):
            number = nums[idx]
            while stack and number < stack[-1][1]:
                index, value = stack.pop()
                check2[index] = True
            stack.append((idx, number))
            
        for idx in range(len(check1)):
            if check1[idx] and check2[idx]:
                return True
        return False