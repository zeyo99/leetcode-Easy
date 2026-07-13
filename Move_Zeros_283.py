from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        #"-> None" 表示此函式不會回傳任何值，僅修改原始陣列
        """
        不希望宣告一個新陣列來放正確資料(浪費記憶體空間)
        要求原地修改(In place)

        慢指標 (slow)：記錄「下一個非零元素應該要填入的位置」
        快指標 (fast)：負責從頭到尾巡覽整個陣列，尋找非零元素
        """
        slow = 0 #非零元素一定要放最前面
        
        # fast 指標走訪整個array，尋找非零元素
        for fast in range(len(nums)):
            # 當 fast 找到非零元素時，與 slow 位置互換
            if nums[fast] != 0: 
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1 #交換完後，slow指標往前走一格，準備放下一個非零元素
            #同時，fast指標也會繼續往前走，尋找下一個非零元素
            
            #反之若fast指標遇到0，不進行交換，fast繼續往前走

if __name__ == '__main__':
    # 建立測試資料（模擬產線感測器含有無效值 0 的 Log）
    sensor_logs = [0, 1, 0, 3, 12]
    
    print("原始資料:", sensor_logs)
    
    sol = Solution()
    sol.moveZeroes(sensor_logs)
    
    print("清洗後資料:", sensor_logs)
    