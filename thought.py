from operator import attrgetter
import time
import random

class Thought:
	def __init__(self, name, thoughtId, executed, poppable):
		self.name = str(name)
		self.thoughtId = float(thoughtId)
		self.executed = bool(executed)
		self.poppable = bool(poppable)
	def __repr__(self):
		return repr((self.name))
	def pop(self):
		if(self.poppable == True):
			return Thought(self.name, self.thoughtId, True, self.poppable)
		else:
			print("not able to remove thought")


thoughtqueue = [Thought("main", time.time(), False, False)]

print(thoughtqueue)

# while(len(thoughtqueue) != 0):
# 	thoughtqueue[len(thoughtqueue)-1].pop()
# 	rnd = int(random() * 100)
# 	if(rnd <= 25):
# 		thoughtqueue.append(Thought("Thought " + str(rnd), time.time(), False, True))
# 	time.sleep(1)

