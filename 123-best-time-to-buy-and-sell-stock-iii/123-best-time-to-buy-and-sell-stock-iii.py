class Solution(object):
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
	
		dp1 = [0]*len(prices)
		dp2 = [0]*len(prices)
		dp1_max = [0]*len(prices)
		dp2_max = [0]*len(prices)
		
		
		for index in range(1, len(prices)):
			_profit = prices[index] - prices[index -1]
			dp1[index] = max(0, _profit + dp1[index-1])
			dp1_max[index] = max(dp1_max[index-1], dp1[index])
			
		for index in range(len(prices) -2, -1, -1):
			_profit = prices[index + 1] - prices[index]
			dp2[index] = max(0, _profit + dp2[index+1])
			dp2_max[index] = max(dp2_max[index+1], dp2[index])

		
		result = dp2_max[0]
		for index in range(1, len(prices)):
			result = max(result, dp1_max[index-1] + dp2_max[index])
			
		return result