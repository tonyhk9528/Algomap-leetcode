public class 14 {
    class Solution {
        public int maxProfit(int[] prices) {
            int min_i = 0;
            int profit = 0;

            for (int i = 1; i < prices.length; i++) {

                if (prices[i] <= prices[min_i]) {
                    min_i = i;
                } else {
                    if (prices[i] - prices[min_i] > profit)
                    profit = prices[i] - prices[min_i];
                }
            }

            return profit;

        }
    }
}
