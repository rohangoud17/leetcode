class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> myHashMap = new HashMap<>();

        for(int i = 0; i< nums.length; i++){
            int num = nums[i];
            int complement = target - num;

            if(myHashMap.containsKey(complement)){
                return new int[]{myHashMap.get(complement), i};
            }
            myHashMap.put(num, i);
        }
        return new int[]{};
        
    }
}