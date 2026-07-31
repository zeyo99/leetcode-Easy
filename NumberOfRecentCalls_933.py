from collections import deque
import sys
'''
python 的deque是雙向佇列(double-ended queue)，支援從兩端插入和刪除元素，時間複雜度為 O(1)。
原本的quene是單向佇列，只能從一端插入，另一端刪除，刪除第一個時剩下的資料都要往前移，時間複雜度為 O(n)。
'''
class RecentCounter:
    def __init__(self):
        # 初始化一個空的雙向佇列，用來裝「晶圓通過的時間」
        self.q = deque() #若不加.self，則q會被視為區域變數，無法在其他方法中使用
        #
    def ping(self, t: int) -> int: # ping可以理解為「晶圓通過的時間戳記」或 事件觸發
        # 1. 新的晶圓通過了，把時間 t 從尾端塞進紀錄裡
        self.q.append(t)
        
        # 2. 檢查最舊的紀錄有沒有過期 (小於 t - 3000)
        # 注意這裡：必須確保佇列有東西 (self.q)，且最前面的時間 (self.q[0]) 過期了
        while self.q and self.q[0] < t - 3000: #在python語法中，物件可以直接作為True/False值判斷，空的deque會被視為False
            self.q.popleft()  # 從最前面把過期的紀錄踢掉
            
        # 3. 踢完過期品後，佇列裡剩下的長度，就是這 3 秒內的總數量
        return len(self.q)

# --- 以下是你必須自己手寫的 HackerRank 主程式 ---
if __name__ == '__main__':
    counter = RecentCounter()  # 開機：初始化感測器
    
    # 模擬產線一直運轉，不斷讀取新進來的時間戳記
    for line in sys.stdin:
        t = int(line.strip())      # 讀取當下那一行的時間戳記
        result = counter.ping(t)   # 呼叫你的邏輯
        print(result)              # 把結果印出來給系統驗證