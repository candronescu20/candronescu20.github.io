import time
import sys

name = input("To begin our journey, what is your name? ")

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.085)

def greeting():
        delay_print("Salutations " + name + ".\nYour story begins on a perfectly average Sunday and you, " + name + ", are a perfectly average person...")
        time.sleep(0.75)
        delay_print("however at precisely 7:36PM, something changes.\nThoughts of Frosted Flakes consume your mind, everything has suddenly narrowed down to the prospect of one (1) bowl of cereal.\nYou make your way to the kitchen.\nThe cereal, the bowl, and the spoon are all easy to find but when the time comes to seek the milk...")
        time.sleep(1)
        delay_print("\n...It's not there?")
        time.sleep(1)
        delay_print("\nHow could this be?")
        time.sleep(1)
        delay_print("\nYou're out of milk.")
        actDepression()

def actDepression():
    time.sleep(1.5)
    decision1 = input("\nWell, " + name + ", do you continue to act upon your cereal craving or reppress it like all other emotions in your life? Type '1' for act or '2' for reppress: ")
    if (decision1 == '1'):
        delay_print("Good choice. You find your keys and hightail it to the nearest grocery store.")
    elif (decision1 == '2'):
        delay_print("Reconsider your life choices. You will have to go to the store like a functioning human.")
        actDepression()
    else:
        delay_print("Listen up smarty. I said to pick either 1 or 2. Let's try it again.")
        actDepression()
    time.sleep(1)
    delay_print("\n\nYou've made it to Generic Grocery Store.\nAs you amble your way towards the dairy section, you realize something is very wrong.\nRow after row of empty dairy shelves greet you. If you want that bowl of cereal, you must make a decision. ")
    atStore()
    
def atStore():
    decision2 = input("\nDo you ask an associate about the missing milk or do your emotions get the best of you and throw a tantrum? Type '1' for ask or '2' for tantrum: ")
    if (decision2 == '1'):
        delay_print("You ask an associate. He nods and seems to understand your question.\nHe wordlessly motions you to follow him to the back of the store. ")
    elif (decision2 == '2'):
        delay_print("Are you done?")
        time.sleep(1)
        delay_print(" Pick yourself up off the floor and use those defunct social skills.")
        atStore()
    else:
        delay_print("Look, either '1' or '2,' pick one.")
        atStore()
    delay_print("The associate leads you to the unmarked door of a storage room.\nHe unlocks the door, revealing a massive refrigerated warehouse filled with crates of...milk?\nAt last, the end is near and the milk is here.\nThe associate attempts to get your attention again. He asks you a question:\n'So you want soy or 2%?'")
    soyOr2percent()
    
def soyOr2percent():
    decision3 = input("\nType '1' for soy or '2' for 2%: ")
    if (decision3 == '1'):
        delay_print("Compras la botella de leche y luego vuelves a tu casa.\nPones la botella de leche arriba del mostrador, y buscas por el cereal.\nEncuentras la caja de Frosted Flakes. Sacudes la caja...")
        time.sleep(1.5)
        delay_print("\n\n...una escama solitaria se cae de la caja...")
        time.sleep(2)
        delay_print("\n\n\nLa vida no tiene sentido.")
        return True
    elif (decision3 == '2'):
        delay_print("You buy the bottle of milk and return home.\nYou set your hard-won milk on the kitchen counter, now searching for the cereal.\nYou find the box of Frosted Flakes and shake it over your empty bowl...")
        time.sleep(1.5)
        delay_print("\n\n...one solitary flake falls out...")
        time.sleep(2)
        delay_print("\n\n\nLife is meaningless.\n")
        return True
    else:
        delay_print("Try again.\nIntentalo de nuevo.")
        soyOr2percent()
    
greeting()

input("\n\nPress enter to exit. ")