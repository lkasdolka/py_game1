class GiantRoom(object):
	def __init__(self):
	# True or False
	#	self.isGiantAlive = true
		self.isGiantAlive = True
		self.isYouAlive = True
	def intro(self):
		print "You enter the Giant room, there is only one exit door, which is watched by a  cruel giant."
	def hint(self):
		print "what you can do includes: tease,throw,stab,or others."
	def tease(self):
		print "You tease at the giant and you are ignored."
		
	def throw(self):
		print "You throw a stone at him, and piss him off, you got tore apart by the giant."
		self.isYouAlive = False
	def stab(self):
		print "You stab the butts of giant with a pike, and kill him. and you can pass the door now."
		self.isGiantAlive = False	
	def other(self):
		print "I don't know what you say."
		