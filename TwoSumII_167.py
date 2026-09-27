import sys

'''
此題與 Two Sum 類似，但這題的數列是已經排序好的
故省去hash table的空間，改用雙指標法 (Two Pointers) 來解題
'''
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1
        #一前一後

        # 只要兩個指標還沒相撞，就繼續找(否則就找不到了>>return [])
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                # 題目特規要求 1-indexed (從 1 開始算)，所以 index 都要 + 1
                return [left + 1, right + 1]
            elif current_sum > target:
                right -= 1  # 太大，右指標退一步
            else:
                left += 1   # 太小，左指標進一步
                
        return []

# --- HackerRank 主程式標準模板 ---
if __name__ == '__main__':
    input_data = sys.stdin.read().splitlines()
    if len(input_data) >= 2:
        numbers = list(map(int, input_data[0].split()))
        target = int(input_data[1].strip())
        
        solution = Solution()
        result = solution.twoSum(numbers, target)
        print(" ".join(map(str, result)))

'''
對撞指標 (左右往中間)： 專門用來處理「已排序陣列的配對 / 總和問題」。因為一左一右，你才有辦法根據「太大」或「太小」，明確決定是左邊進一步（總和變大）還是右邊退一步（總和變小）。

同向快慢指標： 專門用來處理「陣列元素的覆寫與搬移」（例如你之前寫過的 LeetCode 26 移除重複元素），或是尋找「連續區間」的滑動窗口。它無法解決跳躍式的配對問題。
'''