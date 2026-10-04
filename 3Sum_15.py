import sys

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # 1. 絕對必要的第一步：排序 (時間複雜度 O(N log N))
        nums.sort() #底層使用 Timsort，平均時間複雜度 O(N log N)，最壞情況 O(N log N)，最好的情況 O(N)
        result = []
        
        # 2. 定海神針 i：負責決定第一個數字
        # 為什麼只跑到 len(nums) - 2？因為右邊至少要留兩個位置給 left 和 right
        for i in range(len(nums) - 2): #從陣列的第一個數字開始，直到倒數第三個數字結束  
            
            # 【外層防呆】：如果現在的數字跟上一個一樣，直接跳過，避免產生重複的第一個零件
            if i > 0 and nums[i] == nums[i - 1]: #已排序，若兩數字相同，則會連續出現，直接跳過即可
                #必須考慮 i > 0，否則 nums[i - 1] 會取到負數索引，造成 IndexError
                continue #跳過這次迴圈，進入下一個 i 的迴圈
                
            # a + b + c = 0  =>  target = - a = b + c
            target = -nums[i]
            
            # 3. 降級成 Two Sum II：派出左右指標
            left = i + 1 #左指標從 i 的下一個位置開始，避免重複使用 nums[i]
            right = len(nums) - 1
            
            while left < right:
                current_sum = nums[left] + nums[right]
                
                if current_sum == target:
                    # 找到完美平衡的三個零件了，加進清單
                    result.append([nums[i], nums[left], nums[right]]) #result原本是空的，把找到的三個數字組合加進去
                    
                    # 【內層防呆】：找到一組答案後，left 往右移，但如果下一個數字長得一樣，繼續跳過
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # 【內層防呆】：同理，right 往左移，跳過重複數字
                    while left < right and right > 0 and nums[right] == nums[right - 1]:
                        right -= 1          #確保nums[right-1]不會取到負數索引

                    '''
                    外層的 while left < right :決定是否開啟這輪迴圈
                    內層的 while left < right :確保 left 和 right 不會越界，避免出現 IndexError。
                    '''    
                    # 確實跳過重複值後，指標各自再往前一步，尋找下一種可能的組合
                    left += 1
                    right -= 1

                    '''
                    若找到答案(current_sum == target)，則： 
                    1. 先把答案加進 result
                    2. 跳過重複值(nums[left] == nums[left + 1] 或 nums[right] == nums[right - 1])
                    3. left 再往右移，right 再往左移，尋找下一組可能的答案
                    '''
                elif current_sum < target:
                    left += 1  
                else:
                    right -= 1 
                    
        return result

'''
不排序直接跑三層迴圈之時間複雜度>> O(N^3)
排序後: 排序 O(NlogN) + 雙指標 O(N^2) = O(N^2)
'''

# --- HackerRank 主程式標準模板 ---
if __name__ == '__main__':
    input_data = sys.stdin.read().splitlines()
    if input_data:
        nums = list(map(int, input_data[0].split()))
        
        solution = Solution()
        results = solution.threeSum(nums)
        
        # 輸出處理：將二維陣列印出，符合機考常見格式
        for res in results:
            print(" ".join(map(str, res)))