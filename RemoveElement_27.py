from typing import List

def removeElement(self, nums: List[int], val: int) -> int: #題目要求要輸出陣列處理後的長度，故回傳型態為 int
        """
        將 nums 中等於 val 的元素移除，並返回新陣列的長度。
        必須在原地修改，空間複雜度為 O(1)。 #即使資料量增加，也不會額外增加記憶體使用量(仍輸出「長度」)
        """
        # k 是慢指標，僅觸發條件才會移動(即遇到非 val 的元素才會移動)
        k = 0 #初始值為0
        
        # fast 指標依序走訪整個陣列，每次都走一格，尋找不等於 val 的元素
        for fast in range(len(nums)):
            if nums[fast] != val:
                # 發現有效資料(沒有要被移除的)，將其移到 k 的位置
                nums[k] = nums[fast]
                k += 1
            #利用覆蓋來實現刪除(因為刪除完後面的資料都要往前移)
            #若找到的元素等於 val，則不做任何操作，它會自動被丟棄，因為 k 不會增加，下一個有效元素會覆蓋掉它
        return k

#在實務上，val如同異常值，利用此方法可將異常數據直接原地丟棄，過程中不須再建立暫存空間