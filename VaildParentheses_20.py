import sys

class Solution:
    def isValid(self, s: str) -> bool:
        # 使用 list 作為 Stack
        stack = []
        
        # 建立一個 Hash Map (字典)，將右括號對應到正確的左括號
        # 這能省去寫一堆 if/elif 的麻煩
        mapping = {")": "(", "}": "{", "]": "["}
        #為何要用右括號當 key 呢？因為我們在 Stack 裡面放的都是左括號，當我們遇到右括號時，才需要去比對 Stack 裡的左括號是否正確

        for char in s:#檢查這個字元是不是在 mapping 裡面，如果是右括號就去比對 Stack 裡的左括號是否正確，如果是左括號就直接放進 Stack 裡
            if char in mapping:
                # 情況 A：如果目前這個字元是「右括號」(hash map 裡的 key)
                # 我們就要把 Stack 頂端（最後放進去）的元素彈出來比對
                # 若 Stack 為空，給個虛擬值 '#' 避免報錯
                top_element = stack.pop() if stack else '#' #若stack有東西就把最後一個元素彈出來，若stack是空的就給一虛擬值'#'，避免報錯
                
                # 如果彈出來的左括號，跟字典裡對應的配不上，就宣告失敗
                if mapping[char] != top_element: # 可能是左括號不相符，也可能是之前放入的 "#" - 代表 Stack 是空的，這兩種情況都要回傳 False" 
                    return False
            else:
                # 情況 B：如果目前這個字元是「左括號」
                # 什麼都不用想，直接推入 Stack 裡面等待未來的配對
                stack.append(char)
            #可知左括號會被放進 Stack 裡，右括號會去比對 Stack 裡的左括號是否正確，若不正確就回傳 False，若正確就繼續往下檢查下一個字元

        # 迴圈跑完後，如果 Stack 裡面清空了，代表全數配對成功 (return True)
        # 如果 Stack 裡面還有剩東西，代表有左括號沒被關上 (return False)
        return not stack #stack 為空時，not stack 會是 True，代表配對成功，函式會回傳 True


# --- 以下是 HackerRank 測驗環境的主程式標準模板 ---
if __name__ == '__main__':
    # 假設 HackerRank 的測資是多行字串，例如：
    # ()[]{}
    # (]
    # ([)]
    
    # 讀取標準輸入的所有行，並去除換行符號
    input_data = sys.stdin.read().splitlines()
    
    solution = Solution()
    
    # 針對每一行測資進行處理
    for s in input_data:
        # 如果是空行就跳過 (防呆)
        if not s.strip():
            continue
            
        result = solution.isValid(s)
        
        # 依照 HackerRank 通常的要求，印出小寫的 true 或 false
        print("true" if result else "false")