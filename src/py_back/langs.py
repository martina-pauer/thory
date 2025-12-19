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
        
traslations = Traslator()

def translate(source_words: list, target_words: list): 
    '''
        Translate to the lang by lang code a source of
        word to a target word list of same length
    '''     
    for word_number in range(0, source_words.__len__()):
        traslations.add_traslation(traslations.code, source_words[word_number], target_words[word_number])

initial_words: list = [
                            'Stock', 'Product Name', 'Units In Stock',
                            'Send', 'Price', 'Date', 'Units', 'Name',
                            'Moment', 'Good_Name', 'Available_Units', 'Currency',
                            'inventory_items', 'Total_ARS_Price'
                      ]        
# Decision Map for select translations
lang_map = {
                'es': translate(
                                    initial_words, [
                                                        'Inventario', 'Producto', 
                                                        'Unidades En Inventario', 'Enviar', 
                                                        'Precio', 'Fecha', 'Unidades',   
                                                        'Nombre', 'Momento', 'Producto',
                                                        'Unidades', 'Divisa', 'inventario',
                                                        'Precio_Total_Pesos_Argentinos'
                                                  ]
                               ),                      
# French
                'fr': translate(
                                    initial_words, [
                                                    'Inventaire', 'Produit', 'Unités En Inventaire', 
                                                    'Envoyer', 'Prix', 'Date', 'Unités', 'Nom', 
                                                    'Moment', 'Nom_Des_Merchandise','Unites_Disponibles', 
                                                    'Devise', 'inventaire', 'Prix_Total_Peso_Argentin'
                                                  ]
                          ),                                     
# Deutsch (German)
                'de': translate(
                                  initial_words, [
                                                    'Inventar', 'Produkt', 'Einheiten Im Bestand',  
                                                    'Schicken', 'Preis', 'Datum', 'Einheiten', 
                                                    'Name', 'Momet', 'Name_Des_Produkts',
                                                    'Verfugbare_Einheiten', 'Wahrung', 'inventar',
                                                    'Gesamt-Argentinischer-Preis' 
                                                ]
                              ),                        
# Italian
                'it': translate(
                                    initial_words, [
                                                       'Inventario', 'Prodotto',
                                                       "Unità Nell' inventario", 'Inviare', 'Prezzo', 
                                                       'Data', 'Unità', 'Nome', 'Momento', 'Nome_Del_Prodotto',
                                                       'Unita_Disponibili', 'Valuta', 'inventario', 
                                                       'Prezzo_Totale_Peso_Argentino'
                                                  ]
                              ),     
# Portuguese
                'pt':  translate(
                                    initial_words, [
                                                        'inventário', 'Nome Do Produto', 'Unidades Em Stock', 
                                                        'Enviar', 'preço', 'Data', 'Unidades', 'Nome',
                                                        'Momento', 'Nome_Do_Produto', 'Unidades_Disponiveis', 'Moeda',
                                                        'inventario', 'Preco_Total_Peso' 
                                                   ]
                               ),
# Chinese
                'zh': translate(
                                    initial_words, [
                                                        '存货', '产品名称', '库存单位', 
                                                        '发送', '价格', '日期', '单位', 
                                                        '姓名', '片刻', '产品名称',
                                                        '可用单位', '货币', '存货',
                                                        '总价（阿根廷比索）' 
                                                  ]
                               ),
# Turkish
                'tr': translate(
                                    initial_words,[
                                                        'Envanter', 'Urunun_Ad', 'Stoktaki Birimler', 
                                                        'Gondermek', 'Fiyats', 'Tarih', 'Birimler', 'Isim',
                                                        'An', 'Urunun_Ad', 'Mevcut_Birimler', 'Para_Birimi',
                                                        'envanter', 'Arjantin_cinsinden_toplam_fiyat'
                                                  ]
                               ),
# Russian
                'ru': translate(
                                    initial_words, [
                                                        'запас', 'название продукта',
                                                        'единиц_на_складе', 'отправлять', 'цена', 
                                                        'дата', 'единицы', 'имя', 'момент', 'название_продукта',
                                                        'доступные_единицы', 'валюта', 'запас', 'общая_цена_арс' 
                                                  ]
                              ),
# Ukranian
                'uk': translate(
                                    initial_words, [
                                                        'запас', 'назва продукту', 'одиниць_на_складі', 
                                                        'відправити', 'ціна', 'дата', 'одиниць', 'назва', 
                                                        'момент', 'назва_продукту', 'доступні_одиниці', 'валюта', 'запас',
                                                        'загальна_ціна_ars' 
                                                  ]
                ),
# Japanese
                'ja' : translate(
                                    initial_words, [
                                                                                                            'ストック', '製品名', '在庫単位', 
                                                      '送信', '価格', '日付', '単位', '名前', 
                                                      '一瞬', '製品名', '利用可能な単位', '通貨', 
                                                                                                            'ストック', '合計ars価格'
                                                  ]
                               )                   
         }
lang_map.get(traslations.code)