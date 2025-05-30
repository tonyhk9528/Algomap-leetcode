class Solution {
    public int findClosestNumber(int[] nums) {
        int answer = nums[0];
        for (int i = 1; i < nums.length; i++) {

            if (Math.abs(nums[i]) < Math.abs(answer)) {

                answer = nums[i];

            } else if (nums[i] >= 0 && Math.abs(answer) == Math.abs(nums[i])) {

                answer = nums[i];

            }
    
        }

        return answer;
    }
}