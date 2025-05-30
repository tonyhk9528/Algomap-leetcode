import java.util.ArrayList;
import java.util.List;

public class 238 {
    class Solution {
        public int[] productExceptSelf(int[] nums) {

            int n = nums.length;
            int l_factor = 1;
            int r_factor = 1;
            
            result = int[n];

            for (int i = 0; i < n; i++) {
                result.add(i, 0);
            }


            for (int i = 0; i < n; i++) {
                left.set(i, l_factor);
                l_factor *= nums[i]; 
            }

            for (int j = n - 1; j >= 0; j--) {
                right.set(j, r_factor);
                r_factor *= nums[j];                 
            }

            return result;
            
        }
    }
}
