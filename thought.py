from operator import attrgetter
import time

class Thought:
	def __init__(self, name, thoughtId, executed, poppable, context):
		self.name = str(name)
		self.thoughtId = float(thoughtId)
		self.executed = bool(executed)
		self.poppable = bool(poppable)
		self.context = context
	def __repr__(self):
		return repr((self.name))
	def pop(self):
		if(self.poppable == True):
			return Thought(self.name, self.thoughtId, True, self.poppable, self.context)
		else:
			print("not able to remove thought")


class Context:
	def __init__(self, name, inputs):
		self.name = str(name)
		self.inputs = inputs
	def __repr__(self):
		return repr((self.name))


thoughtqueue = [Thought("main", time.time(), False, False)]

print(thoughtqueue)

