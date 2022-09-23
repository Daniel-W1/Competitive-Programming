class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        okay so we are going to use a hashmap to store all the numbers
        
        and going through each of the numbers we check if we can have num-1 
        in the hashmap if so we don't do anything on that number 
        
        i think we can optimise the space by using a set and  check whther our element exists in the set before we do anything
        
        so for the first test case for example 
        set = {100, 4, 200, 1, 3, 2}
        
        let's go over all the numbers now
        check if we have num - 1 in the set if so just continue
        
        if we don't check how much long sequence we can get by starting from that number and update our answer
        '''
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak
    
    # time comp is O(n) our for loops goes through the whole thing once and 
    # our while loop worst case goes through all of them once so ya O(2n)`O(n)
    
    # space comp is also O(n) because of the set