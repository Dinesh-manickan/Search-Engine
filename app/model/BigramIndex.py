
class BigramIndex:
    def __init__(self,Documents):
        self.Documents=Documents

    def GenerateBigramIndex(self):
        Documents = {}
        for document in self.Documents:
            if document not in Documents.keys():
                Documents[document]=[]
            Bigram = self.BigramIndexBuilder(self.Documents[document])
            Documents[document].append(Bigram)
        return Documents

    def BigramIndexBuilder(self, text, k=2): 
        kgrams = {}
        for word in text:
            for i in range(len(word) - k + 1):
                Bigram = word[i:i+k] 
                if Bigram not in kgrams.keys():
                    kgrams[Bigram]=[]

                if word not in kgrams[Bigram]:
                    kgrams[Bigram].append(word)

        return kgrams 