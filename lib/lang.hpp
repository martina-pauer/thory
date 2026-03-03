class Dict
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
// Create Object
Traslator translation = Traslator();
// Define Words
std :: string[14] init_words = 
                {
                    "Stock", "Product Name", "Units In Stock", "Send", "Price", 
                    "Date", "Units", "Name", "Moment", "Good_Name", "Available_Units", 
                    "Currency", "inventory_items", "Total_ARS_Price"
                };

std :: string[14] es_words =
                {
                    "Inventario", "Producto", "Unidades En Inventario", "Enviar", "Precio",
                    "Fecha", "Unidades", "Nombre", "Momento", "Producto", "Unidades_Disponibles",
                    "Divisa", "inventario", "Precio_Total_Pesos_Argentinos"
                };

std :: string[14] fr_words =
                {
                    "Inventaire", "Produit", "Unités en Inventaire", "Envoyer", "Prix",
                    "Date", "Unités", "Nom", "Moment", "Nom_Des_Merchandise",
                    "Unites_Disponibles", "Devise", "Inventaire", "Prix_Total_Peso_Aregntin"
                };

std :: string[14] de_words =
                {
                    "Inventar", "Produkt", "Einheiten Im Bestand", "Schicken", "Preis",
                    "Data", "Einheiten", "Name", "Moment", "Produkt", "Verfugbare_Einheiten",
                    "Wahrung", "Inventar", "Gesamt-Aregentinisher-Preis"
                };

std :: string[14] it_words =
                {
                    "Inventario", "Prodotto", "Unita Nell' Inventario", "Inviare", "Prezzo",
                    "Data", "Unita", "Nome", "Momento", "Prodotto", "Unita_Disponibili",
                    "Valuta", "Inventario", "Prezo_Totale_ARS"
                };
// Setup Translations
for (unsigned int word_index = 0; word_index < 14; word_index++)
{ // spanish
    translation.add_translations("es", init_words[word_index], es_words[word_index])
}

for (unsigned int word_index = 0; word_index < 14; word_index++)
{
    translation.add_translations("fr", init_words[word_index], fr_words[word_index])
}

for (unsigned int word_index = 0; word_index < 14; word_index++)
{
    translation.add_translations("de", init_words[word_index], de_words[word_index])
}

for (unsigned int word_index = 0; word_index < 14; word_index++)
{
    translation.add_translations("it", init_words[word_index], it_words[word_index])
}
// Now only use translation.translate method for get the text