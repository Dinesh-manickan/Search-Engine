
class InvertedIndex:
    def __init__(self,DoucumentCount,Documents):
        self.DoucumentCount=DoucumentCount
        self.Documents=Documents

    def GenerateInvertedIndex(self):
        InvertedIndex={}
        for index, Document in enumerate(self.Documents.keys(),self.DoucumentCount):
            for word in self.Documents[Document]:
                if len(word)>1:
                    if word not in InvertedIndex:
                        InvertedIndex[word] = {"freq": 0, "postings": []}

                    if index not in InvertedIndex[word]["postings"]:
                        temp = InvertedIndex[word]
                        temp['postings'].append(index)
                        temp['freq']=len(temp["postings"])
                        InvertedIndex[word]=temp

        return InvertedIndex
    
    def SearchInvertedIndex(self,term):
        InvertedIndex = self.GenerateInvertedIndex()
        results={}
        for key, value in InvertedIndex.items():
            if key == term:
                results[key]=value
        return results