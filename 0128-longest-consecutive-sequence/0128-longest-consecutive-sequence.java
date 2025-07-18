class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> mySet = new HashSet<>();
        for(int num: nums){
            mySet.add(num);
        }

        int seqLen = 0;
        for(int i : mySet){
            
            if(!(mySet.contains(i-1))){
                int currNum = i;
                int currentStreak = 1;
                while(mySet.contains(currNum+1)){
                    currNum++;
                    currentStreak++;
                }
                seqLen = Math.max(currentStreak, seqLen);
            }
            


        }
        return seqLen;
        
    }
}