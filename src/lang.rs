pub struct Traslator
{
    // Atributes
  // Dictionary with lang code and list of two translated words
    priv mut words : (&str, (&str, &str));
}
// Methods
impl Traslator
{
    pub translate(&self, word : &str) -> &str
    {
        // Translate the word searching in the list coincidence in first word
        for translation in self.words.1
        {
            if translation.0 == self.words
            {
                return self.words.1.1;
            }
        }
        // If Aren't available translations come here then return the same word
        return word;
    }

    pub add_translations(&mut self, lang_code : &str, init_word : &str, end_word : &str)
    {
        // Add a translations for a language
        self.word.0.push(lang_code)
        self.words.1.push(init_word, end_word);
    }
}
// Create Object
let mut translate = Traslator {words : ()};
// Create list of initial words
let initial_words : [&str; 14] = [
                                    "Stock", "Product Name", "Units In Stock", "Send", 
                                    "Price", "Date", "Units", "Name", "Moment", "Good_Name",
                                    "Available_Units", "Currency", "Inventory_items", "Total_ARS_Price"
                                ];
// Create list of translation
let es_words : [&str; 14] = [
                                "Inventario", "Producto", "Unidades En Inventario", "Enviar", 
                                "Precio", "Fecha", "Unidades", "Nombre", "Momento", "Producto", 
                                "Unidades_Disponibles", "Divisa", "Inventario", "Precio_Total_Pesos_Argentinos"
                            ];
let fr_words : [&str; 14] = [
                                "Inventaire", "Produit", "Unités En Inventaire", 
                                "Envoyer", "Prix", "Date", "Unités", "Nom", 
                                "Moment", "Nom_Des_Merchandise", "Unites_Disponibles", "Devise", "Inventaire", "Prix_Total_Peso_Argentin"
                            ];
let de_words : [&str; 14] = [
                                "Inventar", "Proukt", "Einheiten Im Bestand", "Schicken", 
                                "Preis", "Datum", "Einheiten", "Name", 
                                "Moment", "Name_Des_Produkts", "Verfugbare_Einheiten", "Wahrung", "Inventar", "Gesamt-Argentinisher-Preis"
                            ];
let it_words : [&str; 14] = [
                                "Inventario", "Prodotto", "Unità Nell' Inventario", 
                                "Inviare", "Prezzo", "Data", "Unità", "Nome", 
                                "Momento", "Nome_Del_Prodotto", "Unita_Disponibili", "Valuta", "Inventario", "Prezzo_Totale_Peso_Argentino"
                            ];
// Set translation in object foreach language
for word_index in 0..=13
{
    translate.add_translation(initial_words[word_index], es_words[word_index]);
}

for word_index in 0..=13
{
    translate.add_translation(initial_words[word_index], fr_words[word_index]);
}

for word_index in 0..=13
{
    translate.add_translation(initial_words[word_index], it_words[word_index]);
}

for word_index in 0..=13
{
    translate.add_translation(initial_words[word_index], de_words[word_index]);
}
// Use Decition map for translate to system language
let code : &str = "es";

match code
{
    "es" => 
    {
        for word_index in 0..=13
        {
            translate.translate(es_words[word_index]);
        },
    }    

    "fr" =>
    {
        for word_index in 0..=13
        {
            translate.translate(fr_words[word_index]);
        },
    }    

    "de" =>
    {
        for word_index in 0..=13
        {
            translate.translate(de_words[word_index]);
        },
    }    

    "it" =>
    {
        for word_index in 0..=13
        {
            translate.translate(it_words[word_index]);
        },
    }   

     _ =>
     {
      // When the language isn't found then use the original words
        translate.translate(initial_words);
     }
}