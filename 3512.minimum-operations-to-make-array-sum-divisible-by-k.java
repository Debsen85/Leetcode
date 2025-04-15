import java.util.Arrays;

class Solution {
    public int minOperations(int[] nums, int k) {
        int sum = Arrays.stream(nums).reduce(0, (x, y) -> x + y);
        return sum % k;
    }
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.minOperations(new int[] {5, 6, 7}, 5));
    }
}