class Solution {
    public int maxAscendingSum(int[] nums) {
        int n=nums.length;
        int sum=nums[0],max_sum=0;
        max_sum=Math.max(max_sum,sum);
        for(int i=0;i<n-1;i++){
            if(nums[i]<nums[i+1]){
                sum+=nums[i+1];
            }
            else{
                sum=nums[i+1];
            }
            max_sum=Math.max(max_sum,sum);
        }
        return max_sum;
    }
}