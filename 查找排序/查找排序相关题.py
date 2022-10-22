# _*_coding:utf-8_*_
# created by Amuu on 2021/9/27

# 两个字符串 s t ，判断 s t 是否能重合

def isAnagram(s, t):
    # ss = list(s)
    # tt = list(t)
    # ss.sort()
    # tt.sort()
    # return ss == tt

    # return sorted(list(s)) == sorted(list(t))  # sort 和sorted 不同

    dict1 = {}  # {'a':1,'b':2}
    dict2 = {}
    for ch in s:
        dict1[ch] = dict1.get(ch, 0) + 1
    for ch in t:
        dict2[ch] = dict2.get(ch, 0) + 1
    return dict1 == dict2


# m*n 二维列表 查找一个数是否存在 列表特性：左小右大 上小下大

def searchMatrix(matrix, target):
    # for line in matrix:
    #     if target in line:
    #         return True
    # return False
    h = len(matrix)
    if h == 0:
        return False
    w = len(matrix[0])
    if w == 0:
        return False
    left = 0
    right = w * h - 1
    while left <= right:
        mid = (left + right) // 2
        i = mid // w
        j = mid % w
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] > target:
            right = mid - 1
        else:
            left = mid + 1
    else:
        return False


# print(searchMatrix([[1,2,3,4,5],[6,7,8,9,11]],5))

# 给定列表与整数，找到列表内两个数之和为此整数，返回下标

def binary_search(li, left, right, val):
    while left <= right:
        mid = (left + right) // 2
        if li[mid][0] == val:
            return mid
        elif li[mid][0] > val:
            right = mid - 1
        else:
            left = mid + 1
    else:
        return None


def twoSum(nums, target):
    # n = len(nums)
    # for i in range(n):
    #     for j in range(i):
    #         if nums[i] + nums[j] == target:
    #             return sorted([i,j])

    # for i in range(len(nums)):
    #     a = nums[i]
    #     b = target - a
    #     if b >= a:
    #         j = binary_search(nums, i + 1, len(nums) - 1, b)
    #     else:
    #         j = binary_search(nums, 0, i - 1, b)
    #     if j:
    #         break
    # return sorted([i, j])

    new_nums = [[num, i] for i, num in enumerate(nums)]
    new_nums.sort(key=lambda x: x[0])
    for i in range(len(new_nums)):
        a = new_nums[i][0]
        b = target - a
        if b >= a:
            j = binary_search(new_nums, i + 1, len(new_nums) - 1, b)
        else:
            j = binary_search(new_nums, 0, i - 1, b)
        if j:
            break
    return sorted([new_nums[i][1], new_nums[j][1]])


print(twoSum([1, 20, 2, 50, 51, 65], 22))
