class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> sum_map = new HashMap<>();
        for(int i = 0; i < nums.length; i++) {
            if(sum_map.containsKey(nums[i])) {
                int[] two_sum = {sum_map.get(nums[i]), i};
                return two_sum;
            }
            sum_map.put(target - nums[i], i);
        }
        return new int[]{-1, -1};
    }
}
