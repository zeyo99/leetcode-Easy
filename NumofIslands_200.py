import sys
from collections import deque #double-ended quene 雙向佇列


def num_islands(grid):
    if not grid or not grid[0]:
        #整個網格為空[] or 有列但沒有行[[]]，都視為沒有島嶼
        return 0

    m, n = len(grid), len(grid[0]) # len(grid[0])代表第一列有幾個元素，即有幾個colums
    count = 0
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1)) #(row, column)
                    #往下, 往上, 往右, 往左
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                count += 1              # 發現一座新島
                grid[i][j] = '0'        # 把這個格子淹掉(改成'0'，避免重複計數)
                queue = deque([(i, j)]) #把這個格子加入佇列，準備進行 BFS
                '''
                引入佇列的目的: 專門紀錄需要進一步探索的格子
                若只在 for 底下檢查一次四周，只能淹掉當前格子與它的鄰居，鄰居的鄰居就無法淹掉了
                故需要一個佇列，專門紀錄需要進一步探索的格子執行BFS，直到整座島嶼都被淹掉
                佇列能在計數的當下，一口氣把同一座的島嶼淹掉，避免重複計數
                '''
                while queue: #若佇列不為空，代表還有格子要處理(以此格子為中心，往四個方向找相鄰的陸地)
                    r, c = queue.popleft() #從佇列最左端取出一個格子，進行 BFS ps:(r,c)是這個格子的座標
                    for dr, dc in directions: #對當前格子四個方向進行 BFS
                        nr, nc = r + dr, c + dc #鄰居的座標
                        if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '1':
                            #列未超出邊界   行未超出邊界        鄰居是陸地

                            grid[nr][nc] = '0'   # 鄰居是陸地>>淹掉，避免重複
                            queue.append((nr, nc)) #把這個鄰居格子加入佇列，之後從他開始繼續擴散

                #一旦queue為空，代表這座島嶼已經被淹掉，BFS結束，回到 for 迴圈繼續找下一座島嶼
    return count



'''
時間複雜度：O(m*n) 其中 m 是行數，n 是列數。每個格子最多被訪問一次。
空間複雜度：O(m*n)，在最壞情況下，佇列中可能存放整行或整列的格子。
'''

def main():
    data = sys.stdin.read().split()
    #.split()：用空白、換行、tab 切開，得到字串 list
    if not data:
        return

    m, n = int(data[0]), int(data[1])
    #原先讀進的是字串，故用 int() 轉成整數
    tokens = data[2:]
    #在程式領域，token 指的是「把一段文字切開後得到的最小單位」
    #從第 3 個元素開始，剩下的全部是地圖資料

    # 相容兩種輸入格式(用token數量判斷是哪種：
    # (a) 每列一個字串 "11000"
    '''
    3 4
    1100
    0100
    0011

    '''
    # (b) 每格用空白分隔 "1 1 0 0 0"
    '''
    3 4
    1 1 0 0
    0 1 0 0
    0 0 1 1

    '''
    if len(tokens) == m:
        grid = [list(row) for row in tokens]
    else:
        grid = [tokens[i * n:(i + 1) * n] for i in range(m)]

    print(num_islands(grid))


if __name__ == "__main__":
    main()