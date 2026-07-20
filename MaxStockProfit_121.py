#Best Time to Buy and Sell Stock
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        找出時間序列中，後高減前低的最大差值(要先買才能賣)。
        """
        # 初始化：價格設為無限大，獲利設為 0
        min_price = float('inf') #一開始設無限大，這樣第一個找到的值就會被更新成新的MIN

        max_profit = 0
        
        for price in prices: #python迴圈可以直接宣告變數並賦值(price)，走訪陣列的過程更新它的值
            # 1. 持續追蹤歷史最低點
            if price < min_price:
                min_price = price #更新最佳進場時機(最低價)
            # 2. 計算如果「今天賣出」，獲利是多少，並與歷史最高獲利比較
            elif price - min_price > max_profit:
                max_profit = price - min_price #更新最佳賣出時機
            #用elie if 是因為兩個事件互斥(若今天是最低價，就不可能是賣出獲利的最佳時機)

            #如果上述條件都不成立，表示今天的價格既不是最低價，也不是賣出獲利的最佳時機，則不做任何操作，繼續走訪下一個價格。
                
        return max_profit

if __name__ == '__main__':
    # 測試情境：模擬機台溫度的變化
    sensor_temps = [7, 1, 5, 3, 6, 4]
    
    sol = Solution()
    profit = sol.maxProfit(sensor_temps)
    
    print(f"最大獲利/溫差: {profit}")
    # 預期輸出: 5 (在 1 時買入，在 6 時賣出，6-1=5)