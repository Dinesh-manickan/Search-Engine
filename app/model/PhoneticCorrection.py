
class PhoneticCorrection:
    def __init__(self,Documents):
        self.Documents=Documents

    def GenerateSoundexIndex(self):
        soundex = {}
        for document in self.Documents:
            for word in self.Documents[document]:
                soundexCode = self.GetSoundexCode(word)
                if soundexCode not in soundex.keys():
                    soundex[soundexCode]=[]
                    
                if word not in soundex[soundexCode]:
                    soundex[soundexCode].append(word)
            return soundex
            

    def GetSoundexCode(self,word):
        # Step 1: Convert the word to uppercase
        word = word.upper()

        # Step 2: retain the first letter
        SoundexCode = word[0]

        # Step 3: Create a mapping of consonants to their corresponding Soundex codes
        SoundexMapping = {
            'B': '1', 'F': '1', 'P': '1', 'V': '1',
            'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
            'D': '3', 'T': '3',
            'L': '4',
            'M': '5', 'N': '5',
            'R': '6'
        }

        # Steps 4 and 5: Encode consonants and remove vowels
        for char in word[1:]:
            if char in SoundexMapping:
                SoundexCode += SoundexMapping[char]

        # Step 6: Ensure the code length is 4 characters
        SoundexCode = SoundexCode.replace('0', '')  # Remove zeros
        SoundexCode = SoundexCode.ljust(4, '0')[:4]  # truncate to 4 characters

        return SoundexCode