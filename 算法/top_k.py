"""
sift 小根堆 有向下调整的属性
"""

def sift(li, low, high):
    temp = li[low]
    i = low
    j = 2*i + 1
    while j <= high:
        if j + 1 <= high and li[j+1] < li[j]:
            j += 1
        if li[j] < temp:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            break
    li[i] = temp

def top_k(li, k):
    heap = li[0:k]
    for i in range(k//2 - 1, -1, -1):
        sift(heap, i, k-1)
    for i in range(k, len(li)):
        if li[i] > heap[0]:
            heap[0] = li[i]
            sift(heap, 0, k-1)
    for i in range(k-1, 0, -1):
        heap[0], heap[i] = heap[i],heap[0]
        sift(heap, 0, i-1)
    return heap

li = [50, 16, 30, 101, 60, 90, 2, 80, 70, 100, 145]
print(top_k(li, 4))
