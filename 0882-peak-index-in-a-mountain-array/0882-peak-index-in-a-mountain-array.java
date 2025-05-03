class Solution {
    public int peakIndexInMountainArray(int[] arr) {
        int ind=0;
        for(int i=1;i<arr.length-1;i++){
            if (arr[i]>arr[i+1] && arr[i]>arr[i-1]){
                ind=i;
                return ind;
            }
        }
        return 0;
    }
}