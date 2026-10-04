import sys

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals:
            return []
            
        # 1. 絕對必要的第一步：按照每個區間的「開始時間」進行排序
        # Python 的 sort 預設就會比對陣列的第一個元素
        intervals.sort()
        
        # 2. 準備一個清單裝結果，並先把第一個區間塞進去當作基準
        merged = [intervals[0]]
        
        # 3. 從第二個區間開始，逐一抓出來比對
        # 注意：Python 的索引是從 0 開始，所以 i = 1 表示第二個區間
        # 也就是 intervals[1]，而 intervals[0] 是第一個區間
        for i in range(1, len(intervals)):
            current = intervals[i]
            last_merged = merged[-1] # 永遠只拿 merged 裡面的「最後一個」來比
            
            # 【判斷重疊】：如果上區間的結束時間 >= 目前區間的開始時間
            if last_merged[1] >= current[0]:    # [index0:開始時間, index1:結束時間]

                # 【防呆合併】：結束時間必須取「兩者最大值」，防止大區間包小區間的誤判 
                last_merged[1] = max(last_merged[1], current[1]) #上個區間的開始時間仍不變，僅更新結束時間，便能完成合併
            else:
                # 沒有重疊，代表這是一個全新的獨立區段，直接整包塞進結果集
                merged.append(current)
                
        return merged

# --- HackerRank 主程式標準模板 ---
if __name__ == '__main__':
    # 假設輸入格式為：每行兩個數字，代表一個區間 (例如 "1 3")
    input_data = sys.stdin.read().splitlines()
    intervals = []
    
    for line in input_data:
        if line.strip():
            start, end = map(int, line.split())
            intervals.append([start, end])
            
    solution = Solution()
    results = solution.merge(intervals)
    
    for res in results:
        print(f"{res[0]} {res[1]}")