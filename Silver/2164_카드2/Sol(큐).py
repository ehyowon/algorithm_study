import queue
N = int(input())
q = queue.Queue()

for i in range(N):
	q.put(i+1)

while q.qsize() > 1:
	q.get()
	a = q.get()
	q.put(a)

print(q.get())
