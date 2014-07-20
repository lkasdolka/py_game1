class DogRoom(object):
	def __init__(self):
		self.youAlive = True
		self.dogAwake = True
	def intro(self):
		print "You enter a room guarded by a savage ThreeHeadDog."
	def hint(self):
		print "possible actions include: hit,tease,sing,other"
	def hit(self):
		print "You hit the dog , but no harm done."
	def tease(self):							
		print "You tease at the dog, and piss him off, you got killed cruelly."
		self.youAlive = False
	def sing(self):
		print "You sing a lullaby,  the dog falls asleep, now you can get passed."
		self.dogAwake = False
	def other(self):
		print "I can't catch you clearly."
		