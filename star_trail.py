inventory = []

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
		dead("You rot away in the darkness. You die of dehydration.")
	

	def explore():
		print "You walk out to find yourself in a corridor. Right or left?"
		
		direct = raw_input("> ")
		
		if (">left" or ">Left") in direct:
			corr_left()
		
		if ( ">right" or ">Right") in direct:
			corr_right()
	
	
	
	
	
	
	
	
	
	
	
def start():
	 print """You wake to find yourself in a grey room. 
	The ceiling is high and the room is narrow.
	You have no recollection of how you got here.
	You wearily stand up, loosing your balance for just a second.
	Do you explore the room or do you leave?
	"""
	room = raw_input("> ")
	
	if ">leave" in room:
		explore()
	
	elif ">explore" in room:
		print "You find a few empty drawers and a towel."
		print "Do you want the keep the towel?"
		
		towel = raw_input("> ")
		
		if ">keep" in towel:
			print "You are a wise hitch-hiker."
			inventory.append("towel")
			hitch = True
			explore()
		else:
			print "You leave through the door."
			explore()
			
start()			