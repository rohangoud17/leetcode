class Solution {
    public int removeElement(int[] nums, int val) {
        int count = 0;
        int i = 0;
        for(int j = 0; j< nums.length;j++){
            if(nums[j] != val){
                int temp = nums[j];
                nums[j] = nums[i];
                nums[i] = temp;
                i++;
                count++;
            }
        }
        return count;
    }
}