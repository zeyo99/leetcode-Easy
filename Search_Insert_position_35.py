import sys
'''
題目要求O(logn)，此複雜度的本質是每一步把問題縮小一半（或固定比例），
又題目之陣列已排序，因此可以用二分搜尋法解題

用左右指針的原因:二分搜尋法的本質是每次都把問題縮小一半，
剩下的部分是一段連續區間。
要描述一段區間，
需要起點跟終點>> L & R
'''

def search_insert(nums, target):
    left, right = 0, len(nums) - 1          # 閉區間(包含左右界) [left, right]

    while left <= right:                    # 還有元素沒檢查("="時，代表還有一個元素沒檢查)
        mid = (left + right) // 2
        # "//"是整數除法，會捨去小數點 
        #index從0開始，除完的結果就是中間的index
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1                  # 答案在右半邊，左界往右移
        else:
            right = mid - 1                 # 答案在左半邊，右界往左移

    return left                             # 第一個 >= target 的位置


def main():
    tokens = iter(sys.stdin.read().split())
    nxt = lambda: next(tokens)

    n = int(nxt())
    nums = [int(nxt()) for _ in range(n)]
    target = int(nxt())

    print(search_insert(nums, target))


if __name__ == "__main__":
    main()