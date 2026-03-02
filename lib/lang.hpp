class Dict()
{
    private:
        std :: string lang_code;
        std :: string[] translations;
    public:
        Dict()
        {
            lang_code = "";
            translations = ["", ""];
        }

        void push(std :: string code, std :: string first, std :: string second)
        {
            this -> lang_code = code;
            this -> translations[0] = first;
            this -> translations[1] = second;
        }

        std :: string get_lang()
        {
            return this -> lang_code;
        }

        std :: string[] words()
        {
            return this -> translations;
        }    
}

class Traslator
{
    public:
        Traslator()
        {
           // List with lang code and list with init and end word 
            this -> words = Dict();
        }

        std :: string translate(std :: string word)
        {
            for (int index = 0; index < sizeof(this -> words) / sizeof(this -> words[0]); index++)
            {
              // Search for a word in original lang in the list  
                for (int translate = 0; translate < sizeof(this -> words[index].words) / sizeof(this -> words[0].words); translate++)
                {
                    if (this -> words[index].words[translate] == word)
                    {
                        return this -> word[index].words[translate];
                    }
                }
            }
            // When don't words found then return the same word
            return word;
        }

        void add_translations(std :: string lang_code, std :: string init_word, std :: string end_word)
        {
            this -> words.push(lang_code, init_word, end_word);
        }
        
    private:
        Dict[] words;
};