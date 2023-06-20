class Anagram:

    def __init__(self, word):
        self.letters = sorted(letter for letter in word)
    
    def match(self, list):
        matching = []
        
        for word in list:
            if sorted([letter for letter in word]) == self.letters:
                matching.append(word)
        
        return matching
            