import sys
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        # 1. 初始化：先計算第一個窗口（前 k 個元素）的總和，並將其設為最大總和
        current_sum = sum(nums[:k])
        max_sum = current_sum
        
        # 2. 窗口開始向右滑動，從 index k 一路滑到陣列尾端
        for i in range(k, len(nums)):
            # 核心邏輯：加上右邊新進窗口的元素，減去左邊滑出窗口的元素
            current_sum = current_sum + nums[i] - nums[i - k]
            
            # 更新最大總和
            if current_sum > max_sum:
                max_sum = current_sum
                
        # 3. 題目要求平均值，最後再除以 k 即可
        return max_sum / k

'''
注意本題要找的是contiguous subarray，是要球連續四個數的最大平均，而非整體最大平均
使用滑動窗口(右進左出一個元素)的方式來計算最大平均值是最有效率的。
'''
if __name__ == '__main__':
    # 假設 HackerRank 測資第一行是 K，第二行是陣列元素用空白隔開
    # 讀取標準輸入 (STDIN)
    input_data = sys.stdin.read().splitlines()
    
    if input_data:
        k = int(input_data[0])
        nums = list(map(int, input_data[1].split()))
        
        # 執行計算
        result = Solution().findMaxAverage(nums, k)
        
        # 輸出結果 (STDOUT)
        print(f"{result:.5f}")