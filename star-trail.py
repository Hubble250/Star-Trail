def dead(why):
	print why, "\nThe End"




def captured():
	print "You have been captured!"
	print "They remove you're blaster and start dragging you to an unknown location."
	print "What do you do?"
	
	action = raw_input("> ")
	
	if "fight" in action:
		print "You manage to knock one of the guards out."
		print "The other puts up more of a fight."
		print "You manage to subdue him, but you've made enough noise to alert more of them."
	
	elif "talk" in action:
		print '"Shut it human!" shouts the guard.'
		print 'We\'ll let the captain sort you out.'
		bridge()
	
	else:
		print """You fail, the guards are now angry.
		They take you to a small dark room and lock the door.
		"""
		dead("You rot away in the barkness. You die of dehydration.")
		
captured()