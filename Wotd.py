import random
from tkinter import *


#wordlist
#TODO make it from an excel

word_list = {
    "abc": "xyz",
    "def": "123"
}
#pick one word
#TODO:update logic for word selection
wotd , wotd_meaning = random.choice(list(word_list.items()))

print (wotd, wotd_meaning)

#display as a pop-up
main = Tk()
main.geometry("300x100")

main.title("WotD")

our_message = f'{wotd} : {wotd_meaning}'
messageVar = Message(main,text = our_message, font = "50")
messageVar.pack()
main.mainloop()

#TODO add button for acknoledgemnt and may be a timer for x sec

