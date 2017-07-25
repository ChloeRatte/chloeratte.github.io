a = 0
				while(a == 0):
					print("Change or Go?")
					user_input = input()
					if user_input == "Change":
						a = 1
						print("You run to work in your clean shirt, but only recieve a glare from your boss. It seems this is the third time this month that you have been late. She fires you.")
					if user_input == "Go":
						a = 1
						print("You decide there is no time to change. You arrive at work on time, but you can here the mocking whispers of your coworkers. Your face flushes and you sit, hoping your day will look up after this.")
			elif user_input == "Work":
				print("You arrive at work early, and get a promototion for all of your timeliness and hard work. Congradulations!")
				e = 1
				##while(e == 0):
			user_input = input()

			if user_input == "Wait":
				e = 1
				print("You wait another thirty minutes before getting a call from your job. This is the third time this month that you've been late, and now you're getting fired. You lose.")
			
			elif user_input == "Walk":
				print("You walk to another station and take the Q train. You get off the subway at your normal time, and realize how tired you are. Maybe you have time for a coffee? But what if you're late-")
				e = 1
				h = 0
			
				while(h == 0):
					print("Coffee or Work?")
					user_input = input()
					if user_input == "Coffee":
						h = 1
						print("You get a steaming cup of coffee and fully appreciate its taste. You take too long appreciating, and now you're late- for the third time this month. You're fired.")
					elif user_input == "Work":
						h = 1
						print("You get to work on time- nothing special, but you managed to not get fired. Not bad!") 
					else:
						print("Please type 'Work' or 'Coffee'")
			else:
				print("Please type 'wait' or 'walk'")
						
			else:
				print("Please type 'Work' or 'Coffee'")
				e = 0			
	else:
		print("Please type 'wait' or 'walk'")
		e = 0




		if j == 1:
				stri = "You reopen the sketchbook."
			else:
				stri = "You see the sketchbook in his bag, and ask him to open it for you. You know you'll find your proof there."