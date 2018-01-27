import nltk
from nltk.corpus import stopwords
import re

class TextUtils:

    #Returns a cleanedup text which doesnt include stopwords and is cleaned up to avoid any special characters
    @staticmethod
    def CleanText(textValue):
        #First run regex and clean word
        textValue = re.sub('[^a-z A-Z 0-9]','',textValue).lower().split()
        print("Text value after print is {0}".format(textValue))
        #ensure stopwords arent included
        textValue = [words for words in textValue if not words in stopwords.words('english')]
        #join and return the text
        return ' '.join(textValue)