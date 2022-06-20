class Solution {
    public int findGCD(int[] nums) {
        int max = 0;
        int min = 1001;
        for (int i = 0; i < nums.length; i++){
            max = Math.max(max,nums[i]);
            min = Math.min(min,nums[i]);
        }
        return dijalgo(min,max);
    }
    int dijalgo(int a,int b){
        if (a == b){
            return a;
        }
        if (a>b){
            return dijalgo(a-b,b);
        }
        return dijalgo(a,b-a);
    }
}