import collections


freq = {}
for i in arr:
if (i in freq):
freq[i] += 1
else:
freq[i] = 1
od = collections.OrderedDict(sorted(freq.items()))
for k, v in od.items():
if (v%2 == 1):
print(k, end=" ")
print("")


if __name__ == "__main__":
    t = int(input())
    for _ in range(int(input())):
        n = int(input())
        arr = input().split()
        for i in range(len(arr)):
            if arr[i] != '':
                arr[i] = int(arr[i])

        # --------------------------------------------------------------
        from collections import Counter

        cnt = Counter(arr)
        for a in cnt.keys():
            if cnt[a] == 1:
                print(a)
        print()

        # --------------------------------------------------------------
        t = t - 1

