class Solution {
    public int longestMonotonicSubarray(int[] arr) {
        int incL=1,decL=1,maxL=1;
        int n=arr.length;
        for(int i=0;i<n-1;i++){
            if(arr[i]>arr[i+1]){
                decL++;
                incL=1;
            }
            else if(arr[i]<arr[i+1]){
                incL++;
                decL=1;
            }
            else{
                incL=1;
                decL=1;
            }
            maxL=Math.max(maxL,Math.max(incL,decL));
        }
        return maxL;
    }
}