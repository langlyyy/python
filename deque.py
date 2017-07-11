
from collections import deque
queue = deque(["Eric", "Kim", "Json"])
lan = queue.append("langly")
print(queue)
queue.append("Graham")
print(queue)

print(queue.popleft())
print(queue)
print(queue.popleft())
print(queue)
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())
print(queue)





