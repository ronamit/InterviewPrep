def candies(n, arr):
    # count number of consecutive ups until current postion
    n_ups = [0 for _ in range(n)]
    for i in range(1, n):
        if arr[i-1] < arr[i]:
            n_ups[i] = n_ups[i - 1] + 1
        else:
            n_ups[i] = 0
    # count number of consecutive downs after current postion
    n_downs = [0 for _ in range(n)]
    for i in range(n-2, -1,-1):
        if arr[i] > arr[i + 1]:
            n_downs[i] = n_downs[i + 1] + 1
        else:
            n_downs[i] = 0
    # find optimal pricing
    pricing = [0 for _ in range(n)]
    for i in range(n):
        pricing[i] = max(n_ups[i], n_downs[i])
    print(pricing)
    sum_price = sum(pricing)
    return sum_price + n

# def candies(n, arr):
#     # for simplicity we solve when the minimal value for candy is 0 and add 1 later to each kid
#     V = [0 for _ in range(n)]
#     for i in range(n - 1, -1, -1):
#         Vp = V.copy()
#         if i == 0 or arr[i - 1] == arr[i]:
#             # in this case we have no restriction
#             v_curr = min([c + V[c] for c in range(n)])
#             V = [v_curr for j in range(n)]
#         elif arr[i - 1] < arr[i]:
#             # we  have a cumulative min from the end
#             v_curr = n**2
#             V[n-1] = v_curr
#             for j in range(n-2, -1, -1):
#                 c = j+1
#                 V[j] = min(v_curr, c + Vp[c])
#                 v_curr = V[j]
#         else:
#             # we  have a cumulative min from the start
#             v_curr = n ** 2
#             V[0] = v_curr
#             for j in range(1, n):
#                 c = j-1
#                 V[j] = min(v_curr, c + Vp[c])
#                 v_curr = V[j]
#         # print(V)
#     ans = min(V) + n # add 1 for each kid
#     return ans

#
# def candies(n, arr):
#     # for simplicity we solve when the minimal value for candy is 0 and add 1 later to each kid
#     V = [0 for _ in range(n)]
#     for i in range(n - 1, -1, -1):
#         Vp = V.copy()
#         for j in range(n):
#             # the candy we gave to previous child:
#             cp = j
#             scan_start = 0
#             scan_end = n - 1
#             if i > 0 and arr[i - 1] < arr[i]:
#                 scan_start = cp + 1
#             elif i > 0 and arr[i - 1] > arr[i]:
#                 scan_end = cp - 1
#             min_val = n ** 2  # arbitrary high inf
#             # note: if the range is empty, then we have inf
#             for c in range(scan_start, scan_end + 1):
#                 min_val = min(min_val, c + Vp[c])
#             V[cp] = min_val
#         print(V)
#     ans = min(V) + n # add 1 for each kid
#     return ans
# #


arr = [2,4,2,6,1,7,8,9,2,1]
# arr = [2,4,3,5,2,6,4,5]
# arr = [2,1,2]
n = len(arr)
print(candies(n, arr))
#
# arr = [2,4,2,6,1,7,8,9,2,1]
# n = len(arr)
# print(candies(n, arr))
#
