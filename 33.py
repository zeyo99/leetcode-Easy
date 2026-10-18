import sys


def search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:                        # target 可能不存在，要查到最後一個
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        '''
        先找升序段，然後再判斷 target 是否在升序段內
        '''
        if nums[mid] < nums[right]:             # 右半 [mid, right] 升序
            if nums[mid] < target <= nums[right]: #target 在右半段
                left = mid + 1
            else: #右半沒有，target 在左半段
                right = mid - 1 #把範圍縮小到左半段
        else:                                   # 左半 [left, mid] 升序
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

    return -1


def main():
    tokens = iter(sys.stdin.read().split())
    nxt = lambda: next(tokens)

    n = int(nxt())
    nums = [int(nxt()) for _ in range(n)]
    target = int(nxt())

    print(search(nums, target))


if __name__ == "__main__":
    main()