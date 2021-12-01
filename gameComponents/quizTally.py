from gameComponents import vars
from PIL import Image


def total(value):
    # do some logic to see which character you selected

    if value == 0:
        vars.character = vars.characters[0]

        print(vars.character)
        print("")
        gamora = Image.open("gamora.jpg")
        gamora.show()

    if value == 10:
        vars.character = vars.characters[1]

        print(vars.character)
        print("")
        captain = Image.open("captain_marvel.jpg")
        captain.show()

    if value == 20:
        vars.character = vars.characters[2]

        print(vars.character)
        print("")
        vision = Image.open("vision.jpg")
        vision.show()

    if value == 30:
        vars.character = vars.characters[3]

        print(vars.character)
        print("")
        scarlet = Image.open("scarlet_wicht.jpg")
        scarlet.show()

    if value == 40:
        vars.character = vars.characters[4]

        print(vars.character)
        print("")
        iron = Image.open("iron_man.jpg")
        iron.show()