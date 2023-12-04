class SpellingCorrection:
    def __init__(self, Documents):
        self.Documents = Documents
        self.row = None
        self.col = None
        self.value = 0

    def GeneratePermutermIndex(self):
        PermutermIndex = {}
        for document in self.Documents:
            for term in self.Documents[document]:
                lower_term = term.lower()  # Store lowercase term
                Rotation = []
                for i in range(len(lower_term) + 1):
                    RotatedWord = lower_term[i:] + '$' + lower_term[:i]
                    Rotation.append(RotatedWord)
                PermutermIndex[lower_term] = Rotation
        return PermutermIndex
    
    def EditDistance(self, MisspelledWord, term):
        self.row = len(MisspelledWord) + 1
        self.col = len(term) + 1

        # Building empty matrix with default value 0 in it
        matrix = [[0 for _ in range(self.col)] for _ in range(self.row)]

        # Referring Aarthi's notes 2nd col that # replacement 
        for i in range(self.row):
            matrix[i][0] = i
        
        for j in range(self.col):
            matrix[0][j] = j
        
        # Refer to ppt 1c from unit 1, slide no 27
        for i in range(1, self.row):
            for j in range(1, self.col):
                if MisspelledWord[i - 1] == term[j - 1]:
                    value = 0
                else:
                    value = 1
                matrix[i][j] = min(
                    matrix[i - 1][j - 1] + value,
                    matrix[i - 1][j] + 1,
                    matrix[i][j - 1] + 1
                )
                minDistance = matrix[i][j]

        return [minDistance, matrix]
    
    def EditDistanceBuilder(self, MisspelledWord):
        results = {"minDistance": float('inf'), "results": [], "misspelledWord": MisspelledWord}
        for document in self.Documents:
            for term in self.Documents[document]:
                editDistance = self.EditDistance(MisspelledWord, term)
                minDistance = editDistance[0]
                minMatrix = editDistance[1]

                result = {
                    "matrix": minMatrix,
                    "suggestion": term
                }

                if minDistance < results["minDistance"]:
                    results["minDistance"] = minDistance
                    results["results"] = [result]
                elif minDistance == results["minDistance"]:
                    if result not in results["results"]:
                        results["results"].append(result)

        return results
    
    def PermutermIndexQuery(self, query):
        query = query.lower()  # Convert query to lowercase for case-insensitive search
        permuterm_index = self.GeneratePermutermIndex()
        
        results = set()
        for terms, rotated_query in permuterm_index.items():
            for item in rotated_query:
                if query in item:
                    results.add(terms)

        return list(results)
