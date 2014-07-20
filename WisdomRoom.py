import random
class WisdomRoom(object):
	def __init__(self):
		self.rightAns = False
		self.count = 0
		
	def intro(self):
		print "Now you enter the wisdom room, you can only pass the room by	answer the question correctly."
		
	def q1(self):
		print "what object has four legs in the morning, two legs at noon, three legs in the evening?"
		while self.count < 2 and self.rightAns == False:
			ans = raw_input(">")
			if ans == "human" or ans == "Human":
				print "Correct!"
				#print self.right
				self.rightAns = True
				#print self.right
			elif self.count < 1:
				print "wrong answer, you can take another shot."
				self.count += 1
			elif self.count == 1:
				print "Wrong again, so stupid you are. you get hit by a lightning and die."
				self.count += 1
	
	def q2(self):
		print "what always goes up and never goes down?"
		while self.count < 2 and self.rightAns == False:
			ans = raw_input(">")
			if ans == "age" or ans == "Age":
				print "Correct."
				#print self.right
				self.rightAns = True
				#print self.right
			elif self.count < 1:
				print "wrong answer, you can take another shot."
				self.count += 1
			elif self.count >= 1:
				print "Wrong answer again, burn in hell!"
				self.count += 1
	def q3(self):
		print "what will you break once you say it?"
		while self.count < 2 and self.rightAns == False:
			ans = raw_input(">")
			if ans == "silence" or ans == "Silence":
				print "Correct"
				#print "self.right:",self.rightAns
				self.rightAns = True
				#print "self.right:",self.rightAns
			elif self.count < 1:
				print "wrong answer, you can take another shot."
				self.count += 1
			elif self.count >= 1:
				print "Wrong answer again,such a pig you are."
				self.count += 1
	def random_question(self,con):
		number = random.randint(1,3)
		if number == 1:
			con.q1(); #q1,q2,q3 are local function which cannot been seen in random_question
		elif number == 2:
			con.q2();
		else: #if number ==3:
			con.q3();
		