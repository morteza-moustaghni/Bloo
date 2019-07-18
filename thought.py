from operator import attrgetter
import time

class Thought:
	def __init__(self, name, thoughtId, executed):
		self.name = str(name)
		self.thoughtId = int(thoughtId)
		self.executed = bool(executed)
	def __repr__(self):
		return repr((self.name))


item1 = Thought("main", 0, False)

while True:
	print(item1)
	time.sleep(1)