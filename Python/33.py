from collections import defaultdict
d, n = defaultdict(list), list(map(int, input().split()))

for i in range(n[0]):
    d[input()].append(i + 1)

for i in range(n[1]):
    print(' '.join(map(str, d[input()])) or -1)




# Takes very long time to execute
# n, m = map(int, input().split())
# listA = list()
# listB = list()

# for i in range(0,n):
#     listA.append(input())

# for i in range(0,m):
#     listB.append(input())

# for i in range(m):
#     for j in range(n):
#         if listB[i] == listA[j] and listB[i] in listA:
#             print(j+1,end=" ")
#         elif listB[i] not in listA:
#             print("-1")
#     print()

