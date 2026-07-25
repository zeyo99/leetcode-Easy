from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        找出出現次數超過一半的多數元素。
        空間複雜度 O(1)，時間複雜度 O(N)
        """
        candidate = None
        count = 0
        
        for num in nums:
            # 如果計數歸零，代表該元素出現次數不足夠多到佔超過1/2，故重新選出候選人
            if count == 0:
                candidate = num #當前元素成為新的候選人
                
            # 判斷當前數字是友軍還是敵軍
            if num == candidate:
                count += 1 #相同元素往上計數
            else:
                count -= 1 #不同元素相互抵消
                
        return candidate

'''
1本題採用摩爾投票法(Moore Voting Algorithm)
其核心概念為不同元素相互抵消，最終剩下的元素即為多數元素。
此方法會設一個候選人(candidate)與計數器(count)，當 count 為 0 時，將當前元素設為候選人，並將 count 設為 1。
若當前元素與候選人相同，則 count +1 ；若不同，則 count -1。最終候選人即為多數元素。

本題假設一定存在多數元素，因此不需要額外驗證候選人是否為多數元素。
'''

if __name__ == '__main__':
    # 模擬產線傳回的異常代碼 Log，其中 '2' 佔了絕大多數
    machine_logs = [2, 2, 1, 1, 1, 2, 2]
    
    sol = Solution()
    majority_code = sol.majorityElement(machine_logs)
    
    print(f"洗版的異常代碼是: {majority_code}")
    # 預期輸出: 2