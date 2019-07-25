#!/usr/bin/python

from nltk.corpus import wordnet
import nltk
from tkinter import *
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from tkinter import filedialog
from PIL import Image
from pytesseract import image_to_string

def P4():
    Tk().withdraw() # Close the root window
    in_path = filedialog.askopenfilename()
    # print(in_path)
    # Image to Text
    stemmer = SnowballStemmer("english")

    string = image_to_string(Image.open(in_path))

    tokens = nltk.word_tokenize(string)
    root = Tk()
    frame1 = Frame(root, width=500, height=5, background="white")
    root.title('P4')
    frame1.pack(fill=None, expand=False)
    for token in tokens:
        synonyms = []
        antonyms = []
        print(token)
        msg_main = Message(root, text = "Word is '" + token +"'")
        msg_main.config(bg='lightgreen', font=('times', 11, 'italic'))
        msg_main.pack()
        for syn in wordnet.synsets(token):
            for l in syn.lemmas():
                synonyms.append(l.name())
                if l.antonyms():
                    antonyms.append(l.antonyms()[0].name())
        msg4 = Message(root, text = "Antonyms")
        msg4.config(bg='white', font=('times', 11, 'italic'), width=1000)
        msg4.pack()
        msg3 = Message(root, text = set(antonyms))
        msg3.config(bg='lightgreen', font=('times', 11))
        msg3.pack()
        msg2 = Message(root, text = "Synonyms")
        msg2.config(bg='white', font=('times', 11, 'italic'), width=1000)
        msg2.pack()
        msg = Message(root, text = set(synonyms))
        msg.config(bg='lightgreen', font=('times', 11))
        msg.pack()

    root.mainloop()

P4()
