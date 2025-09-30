class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        
        while(start <= end):
            midNo = (start + end)//2
            if (nums[midNo] == target):
                return midNo
            elif(target > nums[midNo]):
                start = midNo + 1
            elif(target < nums[midNo]):
                end = midNo - 1
        
        return -1


        