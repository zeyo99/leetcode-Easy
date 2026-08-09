import sys

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # 使用 & 運算子，直接取兩個集合的「交集」
        return list(set(nums1) & set(nums2))
                    #把nums1和nums2轉換成集合，然後使用 & 運算子計算交集，最後再將結果轉換回列表。

    '''
    <sol2>

    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
    # 1. 把 nums1 轉換成 set，後續查詢時間變成 O(1)
        set1 = set(nums1)
        
        # 2. 準備一個空的 set 來裝結果 (確保結果不會重複)
        result_set = set()
        
        # 3. 走訪 nums2，去 set1 裡面查
        for num in nums2:
            if num in set1:
                result_set.add(num)
                
        # 4. 回傳 list
        return list(result_set)
    
    '''
if __name__ == '__main__':
    input_data = sys.stdin.read().splitlines()
    if len(input_data) >= 2:
        nums1 = list(map(int, input_data[0].split()))
        nums2 = list(map(int, input_data[1].split()))
        
        solution = Solution()
        result = solution.intersection(nums1, nums2)
        print(" ".join(map(str, result)))