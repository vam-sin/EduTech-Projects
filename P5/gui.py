from tkinter import *
from tkinter import filedialog
from PIL import Image
from pytesseract import image_to_string
import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
import numpy as np
import nltk
from googlesearch import search
nltk.download('wordnet')

def P5():

    Tk().withdraw() # Close the root window
    in_path = filedialog.askopenfilename()
    # print(in_path)
    # Image to Text
    stemmer = SnowballStemmer("english")

    input_str = image_to_string(Image.open(in_path))

    # print(input_str)

    # Text to Topic

    def lemmatize_stemming(text):
        return stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))

    # Tokenize and lemmatize
    def preprocess(text):
        result=[]
        for token in gensim.utils.simple_preprocess(text) :
            if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
                result.append(lemmatize_stemming(token))

        return result

    output = preprocess(input_str)

    # print(output)
    output = [d.split() for d in output]

    dictionary = gensim.corpora.Dictionary(output)

    corpus = [dictionary.doc2bow(doc) for doc in output]

    lda_model =  gensim.models.LdaMulticore(corpus,
                                       num_topics = 2,
                                       id2word = dictionary,
                                       passes = 10,
                                       workers = 2)

    topics = []

    for idx, topic in lda_model.print_topics(-1):
        m = topic.index('"')
        n = topic.index('+')
        topics.append(topic[m+1:n-2])
        # print("Topic: {} \nWords: {}".format(idx, topic ))
        # print("\n")

    # print("\nTopics")
    # print(topics)
    # print("\n")
    # Topic to reading material

        # print("\n")

    root = Tk()
    frame1 = Frame(root, width=500, height=5, background="white")
    root.title('P5')
    frame1.pack(fill=None, expand=False)
    msg4 = Message(root, text = "Input String")
    msg4.config(bg='white', font=('times', 11, 'italic'), width=1000)
    msg4.pack()
    msg3 = Message(root, text = input_str)
    msg3.config(bg='lightgreen', font=('times', 11, 'italic'), width=1000)
    msg3.pack()

    msg2 = Message(root, text = "Topics")
    msg2.config(bg='white', font=('times', 11, 'italic'), width=1000)
    msg2.pack()
    msg = Message(root, text = set(topics))
    msg.config(bg='lightgreen', font=('times', 11, 'italic'), width=1000)
    msg.pack()

    for a in topics:
        query = a
        read = []
        # print("Results for " + a)
        for j in search(query, tld="co.in", num=10, stop=10):
            read.append(j)
        msg0 = Message(root, text = "Reading Material for {}".format(query))
        msg0.config(bg='white', font=('times', 11, 'italic'), width=1000)
        msg0.pack()
        msg5 = Message(root, text = set(read))
        msg5.config(bg='lightgreen', font=('times', 11, 'italic'), width=1000)
        msg5.pack()

    root.mainloop()


P5()
