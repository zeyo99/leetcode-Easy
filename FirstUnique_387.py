import sys
from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
         #第一次走訪字串，統計每個字元出現的次數並回傳為字典   
        freq_dict = Counter(s)
                    #Counter:元素被儲存為字典的鍵，元素的計數被儲存為字典的值
                    
        # 第二次走訪字串，並搭配 enumerate 取得 Index
        for i, char in enumerate(s):
            # 只要查到這個字元的總次數是 1，它就是我們要找的「第一個」孤立異常
            if freq_dict[char] == 1:
                return i #取得該字元的索引值
                
        # 如果整趟跑完都沒有遇到次數為 1 的字元，代表全都有重複
        return -1


# --- HackerRank 主程式標準模板 ---
if __name__ == '__main__':
    input_data = sys.stdin.read().splitlines()
    
    solution = Solution()
    for s in input_data:
        if not s.strip():
            continue
        print(solution.firstUniqChar(s)) 