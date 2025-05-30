import java.util.ArrayList;
import java.util.List;

public class 228 {
    class Solution {
        public List<String> summaryRanges(int[] nums) {

            StringBuilder range = new StringBuilder();
            ArrayList answer = new ArrayList();

            int prev = nums[0];
            

            range.append(String.valueOf(prev));


            for (int i = 1; i < nums.length; i++) {

                if (nums[i] - prev != 1) {
                    answer.add(range.toString());
                    range.clear
                }


                
            }

            

            return answer;
        }
    }
}



//[0,1,2,4,5,7]