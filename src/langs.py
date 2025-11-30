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
                ('Currency', 'Divisa'), ('inventory_itmes', 'inventario')
                ('Total_ARS_Price', 'Precio_Total_Pesos_Argentinos')       
            ]:
    traslations.add_traslation('es', word[0], word[1])             
# French
for word in [
                ('Stock', 'Inventaire'), ('Product Name', 'Produit'),
                ('Units In Stock', 'Unités En Inventaire'), ('Send', 'Envoyer'),
                ('Price', 'Prix'), ('Date', 'Date'), ('Units','Unités'),   
                ('Name', 'Nom'), ('inventory_items', 'inventaire')
            ]:
    traslations.add_traslation('fr', word[0], word[1])                    
# Deutsch (German)
for word in [
                ('Stock', 'Inventar'), ('Product Name', 'Produkt'),
                ('Units In Stock', 'Einheiten Im Bestand'),  ('Send', 'Schicken'),
                ('Price','Preis'), ('Date', 'Datum'), ('Units', 'Einheiten'), 
                ('Name', 'Name')
            ]:
    traslations.add_traslation('de', word[0], word[1])                    
# Italian
for word in [
                ('Stock', 'Inventario'), ('Product Name', 'Prodotto'),
                ('Units In Stock', "Unità Nell' inventario"), 
                ('Send', 'Inviare'), ('Price', 'Prezzo'), 
                ('Date', 'Data'), ('Units', 'Unità'), ('Name', 'Nome')
            ]:
    traslations.add_traslation('it', word[0], word[1])      
