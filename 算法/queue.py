from collections import deque

q = deque()
q.append(1)
q.append(2)
print(q.popleft())

q.appendleft(3)
q.pop()

x = deque(open("test.txt", "r"), 5)

for i in x:
    print(i,type(i))