from gameComponents import gameVars

def winorlose(status):
	print(" ")
	print("DAD " + status)
	print("Would you like to play RABBIT, GUN & WALL again?... Please Daddy?")
	choice = input(" Y / N? ")

	global DadLives
	global SonLives
	global Dad

	if choice == "n":
		print(" ")
		print("Ok Dad, you must have a lot better things to do ... continue with your busy adult life  :(")
		print(" ")
		exit()
	elif choice == "y":
		print(" ")
		print("Remember... Wall defeats Gun, Gun defeats Rabbit, and Rabbit defeats Wall.")
		print(" ")
		gameVars.DadLives = 5
		gameVars.SonLives = 5
		gameVars.Dad = False