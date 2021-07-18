print("Rock...")
print ("Paper...")
print ("Scissors...")

import random
player = input("Select between rock, paper  and scissors: ").lower()
rand_num = random.randint (0,2)

if rand_num == 0:
	computer = "paper"
elif rand_num == 1:
	computer = "rock"
else:
	computer = "scissors"
print(f"Computer plays {computer}")

# Modificador de Empate
if player == computer:
	print("It's a tie!")
#El jugador elige piedra
elif player == "rock":
	if computer == "scissors":
			print("Player 1 wins!")
	elif computer == "paper":
		print("Player 2 wins!")
#El jugador elige papel
elif player == "paper":
	if computer == "rock":
			print("Player 1 wins!")
	elif computer == "scissors":
			print("Player 2 wins!")
#El jugador elige tijeras
elif player == "scissors":
	if computer == "rock":
		print ("Player 2 wins!")
	elif computer == "paper":
		print ("Player 1 wins!")
else:
	print("Something went wrong")

input ("Please, press Enter to exit")