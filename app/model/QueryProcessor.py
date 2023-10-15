from collections import Counter
from app.model.InvertedIndex import InvertedIndex
from app.model.SpellingCorrection import SpellingCorrection
from app.model.PrecisionRecall import PrecisionRecall

class QueryProcessor:
    def __init__(self, inverted_index, bigram_index, permuterm_index, soundex_index, edit_distance_index, Documents,FileLocation) :
        self.FileLocation = FileLocation
        self.Documents = Documents
        self.inverted_index = inverted_index
        self.bigram_index = bigram_index
        self.permuterm_index = permuterm_index
        self.soundex_index = soundex_index
        self.edit_distance_index = edit_distance_index

    def queryProcessing(self,query,operatorPosition): #using operator
        lhs = query[operatorPosition-1]
        rhs = query[operatorPosition+1]

        misspelledWord = [lhs,rhs]
        data = []
        suggestedWord=[]
        for word in misspelledWord:
            responce = self.editDistance(word)['results']
            for suggestions in responce:
                suggestedWord.append(suggestions['suggestion'])

        for term in suggestedWord:
            data.append(self.SearchInvertedIndex(term))
        return data
    
    def SearchInvertedIndex(self,term):
        return InvertedIndex(DoucumentCount=1,Documents=self.Documents).SearchInvertedIndex(term)
    
    def editDistance(self, MisspelledWord): 
        return SpellingCorrection(self.Documents).EditDistanceBuilder(MisspelledWord)
    

    def findQuery(self,query):
        try:
            ReleventSuggest = PrecisionRecall(self.Documents,query,self.FileLocation)
            print(ReleventSuggest.PRFfunc())
            return ReleventSuggest.PRFfunc()
        except Exception as e:
            print(e)
            return {"error":"No results Found for given query ("+query+")"}
       
        # booleanOperator = ['and', 'or', 'not']
        # query=query.lower().split()
        # responsive={}

        # results=None
        # if booleanOperator[0] in query: # and operation
        #     try:
        #         operatorPosition = query.index(booleanOperator[0])
        #         results = self.queryProcessing(query,operatorPosition)
        #         postings = None
               
        #         for data in results:
        #             for key, values in data.items():
        #                 if key not in  responsive:
        #                     responsive[key]=[]
        #                 responsive[key]=values['postings']
        #                 if postings == None:
        #                     postings=values['postings']
        #                 postings=set(postings) & set(values['postings'])
        #         return {"results":postings,"addons":responsive}
        #     except:
        #         return {"results":""}
        
        # elif booleanOperator[1] in query: # or operation
        #     try:    
        #         operatorPosition = query.index(booleanOperator[1])
        #         results = self.queryProcessing(query,operatorPosition)
        #         postings = None
        #         for data in results:
        #             for key, values in data.items():
        #                 if key not in  responsive:
        #                     responsive[key]=[]
        #                 responsive[key]=values['postings']
        #                 if postings == None:
        #                     postings=values['postings']
        #                 postings=set(postings) | set(values['postings'])
        #         return  {"results":postings,"addons":responsive}
        #     except:
        #         return {"results":""}

        # elif booleanOperator[2] in query: # not operation
        #     try:
        #         operatorPosition = query.index(booleanOperator[2])
        #         results = self.queryProcessing(query,operatorPosition)
        #         postings = None
        #         for data in results:
        #             for key, values in data.items():
        #                 if key not in  responsive:
        #                     responsive[key]=[]
        #                 responsive[key]=values['postings']
        #                 if postings == None:
        #                     postings=values['postings']
        #                 postings=set(postings) - set(values['postings'])
        #                 if not postings:
        #                     postings = values['postings']

        #         return {"results":postings,"addons":responsive}
        #     except:
        #         return {"results":""}

        # else:
        #     try:
        #         misspelledWord = query
        #         data = []
        #         suggestedWord=[]
        #         for word in misspelledWord:
        #             responce = self.editDistance(word)['results']
        #             for suggestions in responce:
        #                 suggestedWord.append(suggestions['suggestion'])
                
        #         joined_query = ' '.join(suggestedWord)
                
        #         for term in suggestedWord:
                    
        #             data.append(self.SearchInvertedIndex(term))
        #         results = data
        #         postings = None
        #         for data in results:
        #             for key, values in data.items():
        #                 if key not in  responsive:
        #                     responsive[key]=[]
        #                 responsive[key]=values['postings']
        #                 if postings == None:
        #                     postings=values['postings']
        #                 postings=set(postings) & set(values['postings'])
                

                
                
        #         return  {"results":postings,"addons":responsive}
        #     except:
        #         return {"results":""}
    
    

        
