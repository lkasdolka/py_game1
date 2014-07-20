import GiantRoom
import DogRoom
import WisdomRoom
import GreedRoom
import sys

print "You are about to start an adventure, are you ready?"
ans = raw_input()
if ans == "n" or ans == "N" or ans == 'no' or ans == 'No' or ans == 'NO':
	sys.exit(1)
elif ans == 'y' or ans == 'Y' or ans == 'yes' or ans == 'YES' or ans == 'Yes':
	pass
else:
	print "I don't know what you're saying."
	exit(1)
	
print "Adventure begins."
print "There road ahead diverge, would you take left or right?"
ans = raw_input()
if ans == 'left':
	gr = GiantRoom.GiantRoom()
	gr.intro()
	while gr.isGiantAlive == True and gr.isYouAlive == True:
		print "do something"
		action = raw_input(">")
		if action == "tease":
			gr.tease()
		#if  elif else:
		elif action == "throw":
			gr.throw()
			#exit(1)
		# elif not else if !	
		elif action == "stab":
			gr.stab()
		elif action == 'hint':
			gr.hint()
		else :
			gr.other()
	if gr.isGiantAlive == False:
		print "you pass this stage !"
	elif gr.isYouAlive == False: 
		print "you are dead , game over."
		exit(1)
		
	print "WisdomRoom lies ahead, would go on?"
	ans2 = raw_input('>')
	if ans2 == 'n' or ans2 == 'N':
		exit(1)
	elif ans2 == 'y' or ans2 == 'Y':
		pass
	else:
		print "don't know your words"
		exit(1)
		
	wr = WisdomRoom.WisdomRoom()
	wr.intro()
	print "get ready for the question! you have two shots."
	print "wr.rightAns:",wr.rightAns
	wr.random_question(wr)
	print "wr.rightAns:",wr.rightAns
	if wr.rightAns == True:
		print "congratulations. you pass all the tests."
	elif wr.rightAns == False:
		print "you are such an idiot,game over."
		exit(1)
elif ans == 'right':
	dr = DogRoom.DogRoom()
	dr.intro()
	while dr.youAlive == True and dr.dogAwake == True:
		action2 = raw_input("do something>")
		if action2 == 'hint':
			dr.hint()
		elif action2 == 'hit':
			dr.hit()
		elif action2 == 'tease':
			dr.tease()
		elif action2 == 'sing':
			dr.sing()
		else:
			dr.other()
	if dr.youAlive == True:
		print "congratulations. you pass the room."
	else:
		print "you died,idiot, game is over"
		exit(1)
		
	print "GreedRoom lies ahead, would go on?"
	ans3 = raw_input('>')
	if ans3 == 'n' or ans2 == 'N':
		exit(1)
	elif ans3 == 'y' or ans2 == 'Y':
		pass
	else:
		print "don't know your words"
		exit(1)
	grr = GreedRoom.GreedRoom()
	grr.intro()
	grr.test()
	
	print "congratulations. you passed all the tests."
	
else:
	print "I don't know what you are saying.."
		
		