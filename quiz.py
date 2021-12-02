from gameComponents.quizQuestions import questions
from gameComponents import vars, quizTally
from PIL import Image
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

print(" ")
print(Back.RED + "SURE YOU LIKE MARVEL SUPERHERO MOVIES!")
print(Back.RED + "LET THIS MAGIC COMPUTER DISCOVER WHICH IS ON YOUR MIND!")
print(" ")
print(Back.BLUE + "1. Choose in your mind one (1) of the following 5 Marvel characters:")
print(Fore.BLUE + "a. GAMORA: Unloyal daughther of Thanos.")
print(Fore.BLUE + "b. CAPTAIN MARVEL: Almighty woman with the hardest forehead in the galaxy.")
print(Fore.BLUE + "c. VISION: The humanoid robot that Ultron always wanted and only Wanda got.")
print(Fore.BLUE + "d. SCARLET WITCH: Without a broom or pointing hat, he has bewitched more than one man, be careful if you are a robot.")
print(Fore.BLUE + "e. IRON MAN: Genius, millionaire, blah, blah ...")
print(Back.BLUE + "2. Next, answer some questions and the magic computer will tell you which character you had in mind, just answer y(yes) or n(no), don't use capital letters")
print(Back.RED + "Lets make magic!")
print(" ")

answer1 = questions["q1"][input(questions["q1"]["question"])]
print(answer1)

vars.quizTotal += answer1
print(Fore.RED + "...........................\n")

answer2 = questions["q2"][input(questions["q2"]["question"])]
print(answer2)

vars.quizTotal += answer2
print(Fore.RED + "...........................\n")

answer3 = questions["q3"][input(questions["q3"]["question"])]
print(answer3)

vars.quizTotal += answer3
print(Fore.RED + "...........................\n")

answer4 = questions["q4"][input(questions["q4"]["question"])]
print(answer3)

vars.quizTotal += answer4
print(Fore.RED + "...........................\n")

print("The magic Number is: " + str(vars.quizTotal) + "\n")
print(Back.RED + "So your Marvel Character is...")

quizTally.total(vars.quizTotal)
