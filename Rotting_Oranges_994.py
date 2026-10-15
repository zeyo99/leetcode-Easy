import sys
from collections import deque


def oranges_rotting(grid):
    m, n = len(grid), len(grid[0])
    queue = deque()
    fresh = 0
    '''
    先紀錄所有x爛橘子，也順便計新鮮橘子
    所有爛橘子同時開始腐爛新鮮橘子，避免多算時間
    (需要新鮮橘子數量判斷是否有得腐爛)
    '''
    # 1. 所有爛橘子一起入佇列（多源），同時數新鮮橘子
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                queue.append((i, j))
            elif grid[i][j] == 1:
                fresh += 1

    minutes = 0
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

    # 2. 一層一分鐘；fresh 歸零就停，避免多算最後一輪
    while queue and fresh > 0:
        for _ in range(len(queue)):          # 只處理「這一層」，即「這一分鐘」所處理的爛橘子
            # 若不關心迴圈當前次數， for 後面可用"-"，代表不需要變數
            r, c = queue.popleft() # 從佇列最左端取出一個爛橘子
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    grid[nr][nc] = 2         # 入佇列時就標記
                    fresh -= 1
                    queue.append((nr, nc)) #下一層的爛橘子，準備在下一分鐘腐爛新鮮橘子
        minutes += 1 #每跑完一層(當前Quene的所有爛橘子都腐爛完新鮮橘子)，就代表過了一分鐘

    # 3. 還有新鮮的就代表到不了
    return minutes if fresh == 0 else -1


def main():
    tokens = iter(sys.stdin.read().split())
    nxt = lambda: next(tokens)

    m, n = int(nxt()), int(nxt())
    grid = [[int(nxt()) for _ in range(n)] for _ in range(m)]

    print(oranges_rotting(grid))


if __name__ == "__main__":
    main()