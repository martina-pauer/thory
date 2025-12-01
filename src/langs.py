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
                ('Stock', '存货'), ('Product Name', '产品名称'),
                ('Units In Stock', '库存单位'), 
                ('Send', '发送'), ('Price', '价格'), 
                ('Date', '日期'), ('Units', '单位'), ('Name', '姓名'), ('inventory_items', '存货'),
                ('Available_Units', '可用单位'), ('Currency', '货币'),
                ('Moment', '片刻'), ('Good_Name', '产品名称'),
                ('Total_ARS_Price', '总价（阿根廷比索）') 
            ]:
    # Lang Code, English Word, Translated Word        
    traslations.add_traslation('zh', word[0], word[1])
# Turkish
for word in [
                ('Stock', 'Envanter'), ('Product Name', 'Urunun_Ad'),
                ('Units In Stock', 'Stoktaki Birimler'), 
                ('Send', 'Gondermek'), ('Price', 'Fiyats'), 
                ('Date', 'Tarih'), ('Units', 'Birimler'), ('Name', 'Isim'), ('inventory_items', 'envanter'),
                ('Available_Units', 'Mevcut_Birimler'), ('Currency', 'Para_Birimi'),
                ('Moment', 'An'), ('Good_Name', 'Urunun_Ad'),
                ('Total_ARS_Price', 'Arjantin_cinsinden_toplam_fiyat') 
            ]:
    # Lang Code, English Word, Translated Word        
    traslations.add_traslation('tr', word[0], word[1])
# Russian
for word in [
                ('Stock', 'запас'), ('Product Name', 'название продукта'),
                ('Units In Stock', 'единиц_на_складе'), 
                ('Send', 'отправлять'), ('Price', 'цена'), 
                ('Date', 'дата'), ('Units', 'единицы'), ('Name', 'имя'), ('inventory_items', 'запас'),
                ('Available_Units', 'доступные_единицы'), ('Currency', 'валюта'),
                ('Moment', 'момент'), ('Good_Name', 'название_продукта'),
                ('Total_ARS_Price', 'общая_цена_арс') 
            ]:
    # Lang Code, English Word, Translated Word        
    traslations.add_traslation('ru', word[0], word[1])
# Ukranian  
for word in [
                ('Stock', 'запас'), ('Product Name', 'назва продукту'),
                ('Units In Stock', 'одиниць_на_складі'), 
                ('Send', 'відправити'), ('Price', 'ціна'), 
                ('Date', 'дата'), ('Units', 'одиниць'), ('Name', 'назва'), ('inventory_items', 'запас'),
                ('Available_Units', 'доступні_одиниці'), ('Currency', 'валюта'),
                ('Moment', 'момент'), ('Good_Name', 'назва_продукту'),
                ('Total_ARS_Price', 'загальна_ціна_ars') 
            ]:
    # Lang Code, English Word, Translated Word        
    traslations.add_traslation('uk', word[0], word[1])
# Japanese
for word in [
                ('Stock', 'ストック'), ('Product Name', '製品名'),
                ('Units In Stock', '在庫単位'), 
                ('Send', '送信'), ('Price', '価格'), 
                ('Date', '日付'), ('Units', '単位'), ('Name', '名前'), ('inventory_items', 'ストック'),
                ('Available_Units', '利用可能な単位'), ('Currency', '通貨'),
                ('Moment', '一瞬'), ('Good_Name', '製品名'),
                ('Total_ARS_Price', '合計ars価格') 
            ]:
    # Lang Code, English Word, Translated Word        
    traslations.add_traslation('ja', word[0], word[1])
