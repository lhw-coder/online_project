import heapq
import random

li = [5, 7, 8, 9, 1, 3, 2, 4, 6]
heapq.heapify(li)
print(li)
heapq.heappush(li, 0)
print(li)
val = heapq.heappop(li)
print(val)
val1 = heapq.heappop(li)
print(val1)
# print(val)
# print(li)
# val1 = heapq.heappop(li)
# print(val1)
ll = [50, 16, 30, 101, 60, 90, 2, 80, 70, 100, 145]
# print(heapq.nlargest(4, ll))

l = list(range(10000))
random.shuffle(l)
# print(l)
# print(heapq.nlargest(10, l))
# print(heapq.nsmallest(10, l))