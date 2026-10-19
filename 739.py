import sys

'''
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

 
在走訪溫度陣列時，若今天的溫度比前一天高，則前一天的答案就是 1。
若今天的溫度比前一天低，則前一天的答案就不確定
暫時放到stack裡(以索引存入，因索引可直接對應當天溫度(tempature[j])，等到之後有比前一天高的溫度時，再把前一天的答案確定下來。

為何選擇stack? 觀察測資與答案:
那些尚未確定答案並且放入stack的日期，呈現遞減[73, 72, 71, 69]
又stack是先進後出，剛好可以把最晚的日期先確定答案，然後再往前推。
如果今天的溫度比stack頂端的還低(無法達到pop的標準)，那更內層溫度更高，也不用再往內比

pop & push 時機:
pop: 今天溫度比堆疊頂端高
push: 處理完畢後，將今天放入

'''
def daily_temperatures(temperatures):
    n = len(temperatures)
    ans = [0] * n              # 預設 0，留在堆疊裡的不用另外處理
    stack = []                 # 存索引，對應溫度由下到上遞減

    for i, t in enumerate(temperatures):
        # 今天比頂端熱 → 頂端那天的答案確定了
        while stack and t > temperatures[stack[-1]]: #與堆疊最頂端的索引所對應之溫度做比較
            j = stack.pop()
            ans[j] = i - j
        #不比頂端熱>>不進while的比較迴圈，直接加入stack中
        stack.append(i)

    return ans


def main():
    tokens = iter(sys.stdin.read().split())
    nxt = lambda: next(tokens)

    n = int(nxt())
    temperatures = [int(nxt()) for _ in range(n)]

    print(*daily_temperatures(temperatures))   # 空白分隔輸出


if __name__ == "__main__":
    main()