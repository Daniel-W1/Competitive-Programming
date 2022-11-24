class Solution {
    public int hIndex(int[] citations) {
        
        int left = 0, n = citations.length, right = n-1, mid;
        int h_index = 0;
        
        while (left <= right){
            mid = left + (right - left)/2;
            
            if(citations[mid] >= n - mid){
                h_index = n - mid;
                right = mid - 1;
            }
            else{
                left = mid + 1;
            }
        }
        
        return h_index;
        
        
    }
}