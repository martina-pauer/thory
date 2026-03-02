pub struct Traslator
{
    // Atributes
  // Dictionary with lang code and list of two translated words
    priv mut words : (&str, (&str, &str));
}
// Methods
impl Traslator
{
    pub translate(word : &str) -> &str
    {
        // Translate the word searching in the list coincidence in first word
        for translation in words.1
        {
            if translation.0 == words
            {
                return words.1.1;
            }
        }
        // If Aren't available translations come here then return the same word
        return word;
    }

    pub add_translations(lang_code : &str, init_word : &str, end_word : &str)
    {
        // Add a translations for a language
        word.0.push(lang_code)
        words.1.push(init_word, end_word);
    }
}