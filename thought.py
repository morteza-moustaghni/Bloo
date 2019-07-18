from operator import attrgetter

class Thought:
	def __init__(self, name, id, executed):
		self.name = str(name)
		self.id = str(id)
		self.executed = bool(executed)
	def __repr__(self):
		return repr((self.name, self.id, self.executed))

	item1 = Thought("main", "0", False)

	print(item1)