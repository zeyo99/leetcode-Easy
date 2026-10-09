import sys
'''
容積=寬度*高度
在無任何資訊下，先從最大寬度開始>>左右雙指標往內找
1. 雙指標：一個在最左，一個在最右，獲取最大初始寬度
2. 貪婪邏輯：誰矮，誰就往內移(矮的板子真正限制了水位的高度，往內找尋更高的板子)
(犧牲寬度，換取更高的高度，才有可能增加容積)
3. 兩指標相撞時，代表已經找過所有可能的組合，結束迴圈
    此時的最大容積即為答案
'''
class Solution:
    def maxArea(self, height: list[int]) -> int:
        # 1. 雙指標：一個在最左，一個在最右，獲取最大初始寬度
        left = 0
        right = len(height) - 1
        
        max_volume = 0
        
        # 2. 只要左右指標還沒相撞，就繼續尋找
        while left < right:
            # 算出當前的寬度與高度，更新歷史最大容積
            width = right - left
            current_height = min(height[left], height[right]) #木桶效應:矮板子決定水位高度
            current_volume = width * current_height
            
            if current_volume > max_volume:
                max_volume = current_volume
                
            # 3. 貪婪邏輯：誰矮，誰就往內移動，尋找更高的可能性
            if height[left] < height[right]: #決定哪個指標要往內移動
                left += 1
            else:
                right -= 1
                
        return max_volume

# --- HackerRank 主程式標準模板 ---
if __name__ == '__main__':
    # 輸入範例：1 8 6 2 5 4 8 3 7 (一行數字，空白隔開)
    input_data = sys.stdin.read().splitlines()
    if input_data:
        heights = list(map(int, input_data[0].split()))
        
        solution = Solution()
        result = solution.maxArea(heights)
        print(result)