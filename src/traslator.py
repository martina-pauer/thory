class Traslator():

    def __init__():
        '''
            Make automatic custom
            traslations for a software
        '''
        self.lang_dicts: dict = dict()

    def  add_traslation(self, code: str, source_word: str, target_word):
        '''
            Define a new relation between language, star word 
            and end word
        '''
        # Add traslation
        self.langs_dicts.setdefault(code, {source_word : target_word})

    def traslate(self, word) -> str:
        '''
            Give traslation for a word
            only if are defined.
        '''
        try:
            for lang in self.lang_dicts.keys():
                if word in lang.keys():
                    return lang[word]
             # When the word isn't stay in some dictionary
             return word