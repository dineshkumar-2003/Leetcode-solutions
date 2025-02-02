class Solution {
    public boolean check(int[] nums) {
        int n=nums.length;
        if(n<=1) return true;
        int inver=0;
        for(int i=1;i<n;i++){
            if(nums[i]<nums[i-1]){
                ++inver;
            }
        }
        if(nums[0]<nums[n-1]) ++inver;
        return inver<=1;
    }
}