import traslator

traslations = traslator.Traslator()
# Spanish
for word in [
                ('Stock', 'Inventario'), ('Product Name', 'Producto'), 
                ('Units In Stock', 'Unidades En Inventario'), ('Send', 'Enviar'), 
                ('Price', 'Precio'), ('Date', 'Fecha'), ('Units', 'Unidades'),   
                ('Name', 'Nombre'), ('Moment', 'Momento'), 
                ('Good_Name', 'Producto'),
                ('Available_Units', 'Unidades'),
                ('Currency', 'Divisa'), ('inventory_items', 'inventario'),
                ('Total_ARS_Price', 'Precio_Total_Pesos_Argentinos')       
            ]:
    traslations.add_traslation('es', word[0], word[1])             
# French
for word in [
                ('Stock', 'Inventaire'), ('Product Name', 'Produit'),
                ('Units In Stock', 'Unités En Inventaire'), ('Send', 'Envoyer'),
                ('Price', 'Prix'), ('Date', 'Date'), ('Units','Unités'),   
                ('Name', 'Nom'), ('inventory_items', 'inventaire'),
                ('Available_Units', 'Unites_Disponibles'), ('Currency', 'Devise'),
                ('Moment', 'Moment'), ('Good_Name', 'Nom_Des_Merchandise'),
                ('Total_ARS_Price', 'Prix_Total_Peso_Argentin') 
            ]:
    traslations.add_traslation('fr', word[0], word[1])                    
# Deutsch (German)
for word in [
                ('Stock', 'Inventar'), ('Product Name', 'Produkt'),
                ('Units In Stock', 'Einheiten Im Bestand'),  ('Send', 'Schicken'),
                ('Price','Preis'), ('Date', 'Datum'), ('Units', 'Einheiten'), 
                ('Name', 'Name'), ('inventory_items', 'inventar'),
                ('Available_Units', 'Verfugbare_Einheiten'), ('Currency', 'Wahrung'),
                ('Moment', 'Momet'), ('Good_Name', 'Name_Des_Produkts'),
                ('Total_ARS_Price', 'Gesamt-Argentinischer-Preis') 
            ]:
    traslations.add_traslation('de', word[0], word[1])                    
# Italian
for word in [
                ('Stock', 'Inventario'), ('Product Name', 'Prodotto'),
                ('Units In Stock', "Unità Nell' inventario"), 
                ('Send', 'Inviare'), ('Price', 'Prezzo'), 
                ('Date', 'Data'), ('Units', 'Unità'), ('Name', 'Nome'), ('inventory_items', 'inventario'),
                ('Available_Units', 'Unita_Disponibili'), ('Currency', 'Valuta'),
                ('Moment', 'Momento'), ('Good_Name', 'Nome_Del_Prodotto'),
                ('Total_ARS_Price', 'Prezzo_Totale_Peso_Argentino') 
            ]:
    traslations.add_traslation('it', word[0], word[1]) 
# Lang translations Format    
"""
    for word in [
                ('Stock', ''), ('Product Name', ''),
                ('Units In Stock', ''), 
                ('Send', ''), ('Price', ''), 
                ('Date', ''), ('Units', ''), ('Name', ''), ('inventory_items', ''),
                ('Available_Units', ''), ('Currency', ''),
                ('Moment', ''), ('Good_Name', ''),
                ('Total_ARS_Price', '') 
            ]:
    # Lang Code, English Word, Translated Word        
    traslations.add_traslation('', word[0], word[1])
"""      
# Portuguese
for word in [
                ('Stock', 'inventário'), ('Product Name', 'Nome Do Produto'),
                ('Units In Stock', 'Unidades Em Stock'), 
                ('Send', 'Enviar'), ('Price', 'preço'), 
                ('Date', 'Data'), ('Units', 'Unidades'), ('Name', 'Nome'), ('inventory_items', 'inventario'),
                ('Available_Units', 'Unidades_Disponiveis'), ('Currency', 'Moeda'),
                ('Moment', 'Momento'), ('Good_Name', 'Nome_Do_Produto'),
                ('Total_ARS_Price', 'Preco_Total_Peso') 
            ]:
    # Lang Code, English Word, Translated Word        
    traslations.add_traslation('pt', word[0], word[1]) 
# Chinese
for word in [
                ('Stock', ''), ('Product Name', ''),
                ('Units In Stock', ''), 
                ('Send', ''), ('Price', ''), 
                ('Date', ''), ('Units', ''), ('Name', ''), ('inventory_items', ''),
                ('Available_Units', ''), ('Currency', ''),
                ('Moment', ''), ('Good_Name', ''),
                ('Total_ARS_Price', '') 
            ]:
    # Lang Code, English Word, Translated Word        
    traslations.add_traslation('zh', word[0], word[1])
# Turkish
for word in [
                ('Stock', ''), ('Product Name', ''),
                ('Units In Stock', ''), 
                ('Send', ''), ('Price', ''), 
                ('Date', ''), ('Units', ''), ('Name', ''), ('inventory_items', ''),
                ('Available_Units', ''), ('Currency', ''),
                ('Moment', ''), ('Good_Name', ''),
                ('Total_ARS_Price', '') 
            ]:
    # Lang Code, English Word, Translated Word        
    traslations.add_traslation('tr', word[0], word[1])
# Russian
for word in [
                ('Stock', ''), ('Product Name', ''),
                ('Units In Stock', ''), 
                ('Send', ''), ('Price', ''), 
                ('Date', ''), ('Units', ''), ('Name', ''), ('inventory_items', ''),
                ('Available_Units', ''), ('Currency', ''),
                ('Moment', ''), ('Good_Name', ''),
                ('Total_ARS_Price', '') 
            ]:
    # Lang Code, English Word, Translated Word        
    traslations.add_traslation('ru', word[0], word[1])
# Ukranian  
for word in [
                ('Stock', ''), ('Product Name', ''),
                ('Units In Stock', ''), 
                ('Send', ''), ('Price', ''), 
                ('Date', ''), ('Units', ''), ('Name', ''), ('inventory_items', ''),
                ('Available_Units', ''), ('Currency', ''),
                ('Moment', ''), ('Good_Name', ''),
                ('Total_ARS_Price', '') 
            ]:
    # Lang Code, English Word, Translated Word        
    traslations.add_traslation('uk', word[0], word[1])
# Japanese
for word in [
                ('Stock', ''), ('Product Name', ''),
                ('Units In Stock', ''), 
                ('Send', ''), ('Price', ''), 
                ('Date', ''), ('Units', ''), ('Name', ''), ('inventory_items', ''),
                ('Available_Units', ''), ('Currency', ''),
                ('Moment', ''), ('Good_Name', ''),
                ('Total_ARS_Price', '') 
            ]:
    # Lang Code, English Word, Translated Word        
    traslations.add_traslation('ja', word[0], word[1])
# Corean
for word in [
                ('Stock', ''), ('Product Name', ''),
                ('Units In Stock', ''), 
                ('Send', ''), ('Price', ''), 
                ('Date', ''), ('Units', ''), ('Name', ''), ('inventory_items', ''),
                ('Available_Units', ''), ('Currency', ''),
                ('Moment', ''), ('Good_Name', ''),
                ('Total_ARS_Price', '') 
            ]:
    # Lang Code, English Word, Translated Word        
    traslations.add_traslation('', word[0], word[1])
