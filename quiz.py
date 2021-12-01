from gameComponents.quizQuestions import questions
from gameComponents import vars, quizTally
from PIL import Image

print(" ")
print("SURE YOU LIKE MARVEL SUPERHERO MOVIES,")
print("LET THIS MAGIC COMPUTER DISCOVER WHICH IS ON YOUR MIND!")
print(" ")
print("1. Choose in your mind one (1) of the following 5 Marvel characters:")
print("GAMORA: Unloyal daughther of Thanos.")
print("CAPTAIN MARVEL: Almighty woman with the hardest forehead in the galaxy.")
print("VISION: The humanoid robot that Ultron always wanted and only Wanda got.")
print("SCARLET WICTH: Without a broom or pointing hat, he has bewitched more than one man, be careful if you are a robot.")
print("IRON MAN: Genius, millionaire, blah, blah ...")
print("2. Next answer some questions and the magic computer will tell you which character you had in mind, just answer y(yes) or n(no).")
print("Lets make magic!")
print(" ")

answer1 = questions["q1"][input(questions["q1"]["question"])]
print(answer1)

vars.quizTotal += answer1
print("+++++++++++++++++++++++++++++++\n")

answer2 = questions["q2"][input(questions["q2"]["question"])]
print(answer2)

vars.quizTotal += answer2
print("+++++++++++++++++++++++++++++++\n")

answer3 = questions["q3"][input(questions["q3"]["question"])]
print(answer3)

vars.quizTotal += answer3
print("+++++++++++++++++++++++++++++++\n")

answer4 = questions["q4"][input(questions["q4"]["question"])]
print(answer3)

vars.quizTotal += answer4
print("+++++++++++++++++++++++++++++++\n")

print("The magic Number is: " + str(vars.quizTotal) + "\n")
print("So your Marvel Character is...")


# after answer all the questions, figure out who your character is
quizTally.total(vars.quizTotal)
