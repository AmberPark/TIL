lst = [69, 10, 30, 2, 16, 8, 31, 22]

def merge_sort(lst): # 일단 반반씩 나눠
    if len(lst) == 1:
        return lst
    mid = len(lst)//2
    left = lst[:mid]
    right = lst[mid:]
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

# 이건 잘나옴
def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result

print(merge_sort(lst))



# def merge(left, right):
#     result = []
#     idx = 0
#     idx_L = 0
#     idx_R = 0
#     while idx_L < len(left) or idx_R < len(right):
#         if idx_L < len(left) and idx_R < len(right):
#             if left[idx_L] <= right[idx_R]:
#                 result[idx] = left[idx_L]
#                 idx += 1
#                 idx_L += 1
#             else:
#                 result[idx] = right[idx_R]
#                 idx += 1
#                 idx_R += 1
#         elif idx_L < len(left):
#             result[idx] = left[idx_L]
#             idx += 1
#             idx_L += 1
#         elif idx_R < len(right):
#             result[idx] = right[idx_R]
#             idx += 1
#             idx_R += 1
#
#     return result

# print(merge_sort(lst))

