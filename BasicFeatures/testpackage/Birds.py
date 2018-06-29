
class Birds(object):
	members = []
	def __init__(self, name):
		''' Constructor for class Birds. '''
		self.members.append(name)

	def printMembers(self):
		for i in self.members:
			print(i)


