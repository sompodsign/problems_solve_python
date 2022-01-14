# def twoSum(nums, target):
#     x = []
#     for i in range(len(nums)):
#         if nums[i] + nums[i + 1] == target:
#             x.append(i)
#             x.append(i + 1)
#             break
#     print(x)

def twoSum(nums, target):
    checker = {}
    for i, v in enumerate(nums):
        if target - v in checker:
            return [checker[target - v], i]
        else:
            checker[v] = i
    return []


twoSum([2, 7, 8, 15], target=9)
