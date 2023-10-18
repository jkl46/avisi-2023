class _Queue:
	def __init__(self, queueSize):
		self.queue = []
		self.queueSize = queueSize

	def addQueue(self, i):
		self.queue.insert(0, i)
		if len(self.queue) > self.queueSize:
			self.queue = self.queue[0:self.queueSize]

	def dequeue(self):
		return self.queue.pop(-1)

	def printQueueu(self):
		for q in self.queue:
			print(q)

	def fileExport(self, filename):
		with open(filename, 'w+') as f:
			for q in self.queue:
				f.write(str(q))
				f.write('\n')

if __name__ == "__main__":
	q = Queue(10)
	for i in range(20):
		q.addQueue(i)

	q.fileExport('ex.txt')
