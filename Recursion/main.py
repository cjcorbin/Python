

# seen = set()
#
# arr = 1,2,3,4,5,6,7,8,9,5
#
# for i in arr:
#     if i not in seen:
#         seen.add(i)
#     else:
#         print('duplicate', i ,'found')
#
#
#
# #print(arr)
#
# print(seen)

list = []
nMinus1 = 0
nMinus2 = 1

list.append(nMinus1)
list.append(nMinus2)
temp = 0

for i in range (10):
    temp = nMinus2
    nMinus2 = nMinus1 + nMinus2
    nMinus1 = temp
    list.append(nMinus2)

print(list)

