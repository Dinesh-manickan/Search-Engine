from nltk.corpus import *
from nltk.stem import *
from nltk.tokenize import *
import os
import string
import nltk

from app.model.InvertedIndex import InvertedIndex
from app.model.BigramIndex import BigramIndex
from app.model.PhoneticCorrection import PhoneticCorrection
from app.model.SpellingCorrection import SpellingCorrection
from app.model.QueryProcessor import QueryProcessor
from app.model.PrecisionRecall import PrecisionRecall


class model:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words("english"))
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.location = os.path.join(script_dir, '..', 'corpus/')
        self.files = os.listdir(self.location)
        self.DoucumentCount=1

    def ReadFile(self,filename):
        with open(self.location+filename,"r") as f:
            file = f.readlines()
        f.close()
        return file
    
    def RemoveSlashN(self,file):
        Document=""
        for line in file:
            line = line.replace("=", "")
            line = line.replace("'", " '")
            line = line.replace(".", " ")
            line = line.lstrip()
            Document += line.replace("\n", " ")
        return Document
    
    def DataCleansing(self,words):
        cleaned_words = []
        for word in words:
            if word.lower() not in self.stop_words:
                lemma = self.lemmatizer.lemmatize(word.lower())
                if len(word.lower()) > 1:
                    cleaned_words.append(lemma)
        return cleaned_words
    
    def Tokenize(self,file):
        punctuation_to_exclude = ["!", "'", "''", ".", "``", "--"]
        words = word_tokenize(file)
        filtered_tokens = [
            token
            for token in words
            if (
                token not in punctuation_to_exclude
                and token not in string.punctuation
                and not (token.startswith("'") or token.startswith("-"))
            )
        ]
        return filtered_tokens

    def InvertedIndexBuilder(self):
        Documents = self.ReadAllDocuments()
        return InvertedIndex(self.DoucumentCount,Documents).GenerateInvertedIndex()
    
    def SearchInvertedIndex(self,query):
        Documents = self.ReadAllDocuments()
        return InvertedIndex(self.DoucumentCount,Documents).SearchInvertedIndex(query)

    def BigramIndexBuilder(self):
        Documents = self.ReadAllDocuments()
        return BigramIndex(Documents).GenerateBigramIndex()
    
    def PermutermIndexBuilder(self): 
        Documents = self.ReadAllDocuments()
        return SpellingCorrection(Documents).GeneratePermutermIndex()
    
    def PermutermIndexQuery(self,query): 
        Documents = self.ReadAllDocuments()
        return SpellingCorrection(Documents).PermutermIndexQuery(query)
    
    def editDistance(self, MisspelledWord): 
        Documents = self.ReadAllDocuments()
        return SpellingCorrection(Documents).EditDistanceBuilder(MisspelledWord)

    def SoundexIndexBuilder(self): 
        Documents = self.ReadAllDocuments()
        return PhoneticCorrection(Documents).GenerateSoundexIndex()
    
    def ReadAllDocuments(self):
        Documents={}
        for file in sorted(self.files):
            lines = self.ReadFile(file)
            lines = self.RemoveSlashN(lines)
            words = self.Tokenize(lines)
            words = self.DataCleansing(words)
            Documents[file]=words        
        return Documents
    
    def SendDocuments(self):
        sortedDocuments = []
        for file in sorted(self.files):
            sortedDocuments.append(file)
        print(sortedDocuments)
        return sortedDocuments
    

    def queryProcessing(self,query):
        query_processor = QueryProcessor(self.InvertedIndexBuilder(), self.BigramIndexBuilder(), self.PermutermIndexBuilder(), self.SoundexIndexBuilder(), self.SoundexIndexBuilder(), self.ReadAllDocuments(),self.location)
        return query_processor.findQuery(query)
    
    def getDocument(self,id):
        with open(self.location+id, 'r') as file:
            file_content = file.read()
        return [id, file_content]

# obj = IR()
# obj.ReadAllDocuments()