import string
import os
import numpy as np
import nltk
from nltk.tokenize import word_tokenize

class PrecisionRecall:
    def __init__(self,Documents,query, FileLocation) :
        self.Documents=Documents
        self.query=query
        self.FileLocation=FileLocation

    # Function to calculate cosine similarity between two sentences
    def cosine_similarity(self, fileToken,queryToken):

        # Create a set of unique words 
        all_tokens = set(fileToken + queryToken)

        # Create vectors for each sentence based on word frequencies
        vector1 = [fileToken.count(token) for token in all_tokens]
        vector2 = [queryToken.count(token) for token in all_tokens]

        # Calculate the dot product and magnitudes of the vectors
        dot_product = np.dot(vector1, vector2)
        magnitude1 = np.linalg.norm(vector1)
        magnitude2 = np.linalg.norm(vector2)

        # Calculate cosine similarity
        similarity = dot_product / (magnitude1 * magnitude2)

        return similarity

    def PRFfunc(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
            
        CosineScores = {}
        for i in self.Documents:
            fileToken = self.Documents[i]
            query = self.query.lower()
            queryToken = word_tokenize(query)
            score = self.cosine_similarity(fileToken, queryToken)
            score = round(score*10, 2)
            CosineScores[i] = score


        # rank the documents based on scores
        CosineScores = dict(sorted(CosineScores.items(), key=lambda item: item[1], reverse=True))
        
        scores = list(CosineScores.values())
        docID = list(CosineScores.keys())
        threshold = 0.5

        ranked_docs = []
        for i in range(len(scores)):
            ranked_docs.append({"document":docID[i], "scores":scores[i], "path":os.path.join(self.FileLocation,docID[i])})

        total_r, total_nr = 0, 0
        relevant=[]
        nonRelevent = []
        for i in range(len(scores)):   
            if(scores[i]>=threshold):
                total_r = total_r + 1
                relevant.append(ranked_docs[i])
            else:
                total_nr = total_nr + 1
                nonRelevent.append(ranked_docs[i])


        TP = total_r   # True Positive    
        FP = total_nr  # False Positive
        FN = total_r - TP

        if ((TP + FP) == 0):
            Precision = 0.0
        else:
            Precision = round(TP/(TP + FP), 2)   

        if ((TP + FP) == 0):
            Recall = 0.0
        else:
            Recall = round(TP/(TP + FN), 2)

        if ((Precision + Recall) == 0):
            F_Measure = 0.0
        else:
            F_Measure = round(((2*Precision*Recall)/(Precision + Recall)), 2)

        return {
            "results":
                {
                "relevent":relevant,
                "nonRelevent":nonRelevent
                }, 
            "table":{
                "TP":TP,
                "FN":FN,
                "FP":FP,
                "TN":"-"
            },
            "Precision":Precision, 
            "Recall":Recall, 
            "F_Measure":F_Measure
            }
           
