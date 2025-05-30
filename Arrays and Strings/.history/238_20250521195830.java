import java.util.ArrayList;
import java.util.List;

public class 238 {
    class Solution {
        public int[] productExceptSelf(int[] nums) {

            int l_factor = 1;
            int r_factor = 1;
            
            List<Integer> left = new ArrayList<>();
            List<Integer> right = new ArrayList<>();

            for (int i = 0; i < nums.length; i++) {
                left.add(i, 0);
                right.add(i, 0);
            }


            for (int i = 0; i < nums.length; i++) {
                left.set(i, l_factor);
                l_factor *= nums[i]; 
            }

            for (int j = nums.length - 1; j >= 0; j--) {
                right.set(j, r_factor);
                r_factor *= nums[j];                 
            }

            for (int k = 0; k < nums.length; k++) {
                nums[k] = left.get(k) * right.get(k);
            }

            return nums;
            
        }
    }
}
