from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        原地刪除重複元素，返回不重複元素的個數(slow+1)。
        """
        if not nums:
            return 0 #防止系統報錯，若陣列為空，直接回傳 0
            
        slow = 0
        
        # fast 從索引 1 開始往後掃描
        for fast in range(1, len(nums)): 
            if nums[fast] != nums[slow]: # 如果發現跟目前最後一個唯一值不同的新數字
                slow += 1 #慢指針前進，準備放置新的不重複數字
                nums[slow] = nums[fast] #將新的不重複數字放到慢指針的位置，這樣就能保持前面都是不重複的元素
                
        return slow + 1

'''
這個迴圈能作用的原因在於題目說 nums 是 non decreasing order(非遞減排序，及後面數字不得小於前面數字)，所以重複的元素會連續出現。
才能有快慢指針走訪來解題，否則快慢指針就無法正確刪除重複元素，因為重複元素可能散落在陣列中。
'''

if __name__ == '__main__':
    sensor_status = [1, 1, 2, 2, 2, 3, 4, 4, 5]
    
    sol = Solution()
    new_length = sol.removeDuplicates(sensor_status)
    
    print(f"去重後的有效長度: {new_length}")
    print(f"去重後的陣列前段內容: {sensor_status[:new_length]}")
