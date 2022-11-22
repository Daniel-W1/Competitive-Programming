class Solution {
     public int numberOfSubarrays(int[] nums, int k) {
         int left = 0;
         int answer = 0;
         int odd = 0;
         int mididx = -1;
         
         for(int right = 0; right < nums.length; right++){
             if ((nums[right] & 1) == 1){
                 odd++;
             }
             
             if (odd == k && mididx < 0){
                 mididx = right;
             }
             
             while (odd > k){
                 if ((nums[left] & 1) == 1){
                     odd -= 1;
                 }
                 answer += (right - mididx);
                 left ++;
                 
                 if (odd == k){
                     mididx = right;
                 }
                    
             }
         }
         while (odd == k){
             if ((nums[left]&1) == 1){
                 odd -= 1;
             }
             answer += nums.length - mididx ;
             left++;
         }
         return answer;
        
    }
    /*
    left = 0
        answer = 0
        odd = 0
        mididx = -1
        
        for right, num in enumerate(nums):
            if num & 1:
                odd += 1
            
            if odd == k and mididx < 0:
                mididx = right
            
            while odd > k:
                if nums[left] & 1:
                    odd -= 1
                answer += right - mididx
                left += 1
                
                if odd == k:
                    mididx = right
        
        while odd == k:
            if nums[left] & 1:
                odd -= 1
            answer += right - mididx + 1
            left += 1
            
        return answer
    */
   
}