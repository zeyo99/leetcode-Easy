#Find Minimum in Rotated Sorted Array

import sys
'''
可能是
^
|         *
|       *
|    * 
|_* _ _ _ _>
(嚴格遞增)

或
^
|      *   
|    *   
|  *       * 
|_* _ _ _* _>
(有斷層，兩段遞增)
'''

def find_min(nums):
    left, right = 0, len(nums) - 1

    while left < right:                 # 縮到只剩一個位置就停，這個位置就是最小值

        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1              # 斷崖在右邊，mid 不可能是最小
        else:
            right = mid                 # mid 到 right 遞增，mid 可能是最小

    return nums[left]


def main():
    tokens = iter(sys.stdin.read().split())
    nxt = lambda: next(tokens)

    n = int(nxt())
    nums = [int(nxt()) for _ in range(n)]

    print(find_min(nums))


if __name__ == "__main__":
    main()