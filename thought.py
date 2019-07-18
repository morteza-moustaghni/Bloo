from operator import attrgetter

class thought:
	def __init__(self, name, id, executed):
		self.name = str(name)
		self.id = str(id)
		self.executed = bool(executed)
	def __repr__(self):
		return repr((self.name, self.id, self.executed))

	item1 = thought("main", "1", False)

	print(item1)