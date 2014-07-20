class GreedRoom(object):
	def intro(self):
		print "Now you enter the GreedRoom, there is numerous gold here"
		
	def test(self):
		print "if you can take as much as you want, how much would you take?"
		print "please enter a number:"
		ans = raw_input(">")
		if int(ans) < 100:
			print "you are a nice man, you can pass the room now."
		else :
			print "Greed men should be punished, and you left hand is taken apart by death "
			print "Slowly, you died, and game is over"
			exit(1)