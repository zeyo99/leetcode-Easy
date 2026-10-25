import sys
import heapq #python 中的堆疊模組，將一般的list作為"min-heap"
'''
heapq.heappush(heap, item): 加入元素
heapq.heappop(heap)：取出並移除最小的元素。
heap[0]：查看目前最小的元素，但不會移除它。

堆只保證最小值在最前面，其他元素不一定按順序排列。
'''
from collections import Counter


def top_k_frequent(nums, k):
    count = Counter(nums)                   # O(n)：{數字: 次數}
    #紀錄數字出現次數並存成dict
    heap = []                               # min-heap，最多 k 個 (頻率, 數字)
    for num, freq in count.items(): #逐一取出「數字、次數」的配對
        heapq.heappush(heap, (freq, num)) 
        '''
        heappush():把 (freq, num) 放進 heap 
        放入時會自動調整元素位置 確保父節點<=子節點

        因此最小元素(頻率最低者)會在根節點
        下一步就會pop掉它
        '''
        if len(heap) > k:
            heapq.heappop(heap)             # 踢掉頻率最低的

    # heap 內部順序不固定，輸出前依「頻率高到低，同頻率數字小到大」排序
    heap.sort(key=lambda x: (-x[0], x[1]))
    '''
    排序時，對每個元素 x 計算一個排序用的值
    每個x是一組(頻率,數字)>>x[0]:頻率 / x[1]: 數字
    -x[0]把頻率變為負數(這樣做可以讓原本由小到大變成由大到小)
    x[1]則會讓頻率相同時，由小到大排列

    lambda: python裡作為單次運算的簡單函式，不需return會直接回傳結果

    EX: ans = lambda x, y : 2x+ 3y 
    '''
    return [num for freq, num in heap] 
            #遍歷heap裡的每個(num, freq), 只取出數字，組成一個新的, 由num組成的List並回傳


def main():
    tokens = iter(sys.stdin.read().split())
    nxt = lambda: next(tokens)

    n = int(nxt())
    nums = [int(nxt()) for _ in range(n)]
    k = int(nxt())

    print(*top_k_frequent(nums, k))


if __name__ == "__main__":
    main()