import sys

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # 建立一個字典來記錄我們「看過的數字」
        history = {}
        
        for i, num in enumerate(nums):
            # 算出要達到 target，還缺多少
            complement = target - num
            
            # 檢查這個缺的數字，是不是剛剛已經看過了？
            if complement in history:
                # 找到了！回傳歷史記錄裡的 index，以及現在的 index
                return [history[complement], i] #i從0開始算，最先存進history的數字會先被找到，所以會先回傳它的index
                
            # 如果還沒找到，就把現在這個數字跟它的 index 存進字典，留給後面的人配對
            history[num] = i
            
        # 題目保證一定有解，所以理論上不會走到這裡
        return []
'''
先檢查，再加入 才不會出現自己配對自己的情況
EX: nums = [3, 2, 4], target = 6
1. i=0, num=3, complement=3, history={}, 3不在history裡，加入history={3:0}
2. i=1, num=2, complement=4, history={3:0}, 4不在history裡，加入history={3:0, 2:1}
3. i=2, num=4, complement=2, history={3:0, 2:1}, 2在history裡，回傳[1,2]
'''

# --- HackerRank 主程式標準模板 ---
if __name__ == '__main__':
    # 假設 HackerRank 測資有兩行：
    # 第一行是陣列：2 7 11 15
    # 第二行是目標：9
    input_data = sys.stdin.read().splitlines()
    if len(input_data) >= 2:
        nums = list(map(int, input_data[0].split()))
        target = int(input_data[1].strip())
        
        solution = Solution()
        result = solution.twoSum(nums, target)
        
        # 輸出結果，通常要求用空白隔開
        print(" ".join(map(str, result)))