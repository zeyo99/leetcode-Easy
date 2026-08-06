import sys
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        # 使用 set 來當作長度為 k 的滑動窗口
        window = set()
        '''
        dict:內容物是鍵值對>>在乎物件以及其對應的值
        set:內容物只有值，沒有鍵值對>>僅關注物件是否存在

        本題只需要關注物件是否存在，所以使用 set 會比 dict 更省記憶體 
        採用滑動窗口實作
        '''
        for i in range(len(nums)):
            # 1. 維持窗口大小：當 i 超過 k 時，把最左邊「過期」的元素踢掉
            if i > k:
                window.remove(nums[i - k - 1])
                
            # 2. 檢查：如果現在這個數字已經在窗口裡，代表距離一定 <= k
            if nums[i] in window:
                return True
                
            # 3. 若無重複，就把現在這個數字加進窗口
            window.add(nums[i])
            
        return False


if __name__ == '__main__':
    # 模擬輸入兩行測資：
    # 第一行是 nums，用空白隔開：1 2 3 1
    # 第二行是 k：3
    
    input_data = sys.stdin.read().splitlines()
    if len(input_data) >= 2:
        nums = list(map(int, input_data[0].split()))
        k = int(input_data[1].strip())
        
        solution = Solution()
        result = solution.containsNearbyDuplicate(nums, k)
        
        # 依照系統要求，印出小寫的 true 或 false
        print("true" if result else "false")