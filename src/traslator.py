class Traslator():

    def __init__(self):
        '''
            Make automatic custom
            traslations for a software
        '''
        self.lang_dicts: dict = dict()
        # Get and save the language code
        from locale import getlocale
        # Use code of two characters of system language code
        self.code = getlocale()[0][0 : 2]

    def  add_traslation(self, code: str, source_word: str, target_word):
        '''
            Define a new relation between language, star word 
            and end word
        '''
        # Add traslation
        self.lang_dicts.setdefault(code, dict())
        self.lang_dicts[code].setdefault(source_word, target_word)

    def traslate(self, word) -> str:
        '''
            Give traslation for a word
            only if are defined.
        '''
        if self.code in self.lang_dicts.keys():
            return self.lang_dicts[self.code][word]
        else:
            return word