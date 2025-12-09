import langs

tra = langs.traslations

class Good():
    '''
        Represents the inventory good
        with name, available units and
        price:

            Good.name -> str, default class constructor arg
        
            Good.price -> list[str, float], default ARS 3000.00

            Good.count -> int, default 1 unit available
    '''
    def __init__(self, name: str):
        
        self.name: str = name        

        self.price: list[str, float] = ['ARS', 3000.00]

        self.count: int = 1
        
    def fix_types(self):
        '''
            Type correction for security reasons
        '''    
        self.name: str = self.name.__str__()
        
        try:
            self.count: int = int(self.count)
        except:
            print('- Good.count must be still as integer\n')
        try:
            self.price: list[str, float] = [self.price[0].__str__(), float(self.price[1])]
        except:
            print('- Good.price must be a 2 fields tuple text and floating point\n')    
        
    def calc_price(self) -> list[str, float]:
        '''    
            calc the total price for
            this good only (unit times the price)
        '''
        return  [
                    # Mantain the same currency for be more predictible
                    self.price[0], 
                    # Price unit times only with 2 decimals    
                    round(self.count * self.price[1], 2)
                ]

    def convert(self, equiv: float, currency: str):  
        '''
           Make convertion with a equivalence
           value to other currency name
        '''
        self.price[0] = currency
        self.price[1] = round(self.price[1] * equiv, 2)

class Inventory():
    '''
        Define inventory goods and calc the price
        for all the goods and make the sum.

            Inventory.items -> list[Good], All the goods representations
            
            Inventory.goods -> int, How much of each kind of good

            Inventory.count -> int, Total of goods on inventory
    '''
    def __init__(self):
        
        self.items: list[Good] = []

        self.goods: int = 1

        self.count: int = 0

    def update(self):
         '''
            Check that all the properties
            are up to the date
         '''
         if self.count < self.items.__len__():
            for item in range((self.count - 1), self.items.__len__()):
                # Compare with the previous goods for new kinds
                for other in range(0, self.count):
                    different = (self.items[other].name != self.items[item].name)
                # When is different the name to the all the goods then is new
                    if different:
                        # Only count the different to before goods
                        self.goods += 1    
            # Count all the items doesn't matter the kind        
            self.count = self.items.__len__()
         
    def add(self, product: Good):
            '''
                Add a new product to the inventory
                and update data
            '''
            self.items.append(product) 
            self.update() 

    def calc_price(self) -> list[str, float]:
        '''
            Calc the price making the sum 
            of all goods prices
        '''          
        inventory_price: list[str, float] = [self.items[0].price[0], 0.00]
        
        for item in self.items:
            # Sum the prices when are in the same currency
            if (inventory_price[0] == item.price[0]):    
                inventory_price[1] += item.calc_price()[1]      
        # Give as output the resultant price
        return inventory_price 

    def save(self) -> str:
        '''
            Save the info on the inventory
            using a database scheme:

                first level, inventories database
                second level, this inventory database
                third level, each good info tables

            Return the resultant SQL table    
        '''
        # Do table for this inventory in particular
        # Columns in table: moment, good_name, available_units, price, currency
        self.load(f'CREATE TABLE {tra.traslate("inventory_items")} ({tra.traslate("Moment")} timestamp, {tra.traslate("Good_Name")} varchar(255), {tra.traslate("Available_Units")} int, {tra.traslate("Price")} FLOAT(8, 2), {tra.traslate("Currency")} varchar(3), {tra.traslate("Total_ARS_Price")} FLOAT(8, 2));\n')
        # Insert values from this inventory  
        result: str = ''      
        for item in self.items:
                item.fix_types()
                result = self.load(f"INSERT INTO {tra.traslate('inventory_items')}({tra.traslate('Moment')}, {tra.traslate('Good_Name')}, {tra.traslate('Available_Units')}, {tra.traslate('Price')}, {tra.traslate('Currency')}, {tra.traslate('Total_ARS_Price')}) VALUES (datetime('now', 'localtime'), '{item.name}', {item.count}, {item.price[1]}, '{item.price[0]}', {self.calc_price()[1]});\n")
        # Give the table as text to the next process
        return result

    def load(self, command: str) -> str:
        '''
            Load SQL requests with inventory_items table
            with the columns:
                moment,
                good_name, 
                available_units,
                price,
                currency,
                total_ars_price

            Return the text with the data as table.    
        '''
        import sqlite3
        connection = sqlite3.connect(f'{tra.traslate("inventory_items")}.db')
        cursor = connection.cursor()
        # Run with sqlite3
        try:
             # Handle exceptions like table already created or similar
             cursor.execute(command)
             connection.commit()
        except:
             print(f'Mistake in SQL command {command}')
        # Run a select command for make work fetchall method 
        table: str = ''
        try:
            # Format table as text string
            for row in cursor.execute(f'SELECT * FROM {tra.traslate("inventory_items")};'):
                 # Run one time the fetchall method for add rows
                    table += (
                                # Date
                                '\n|  ' + row[0] + '  |  '
                                # Name of product
                                + row[1] + '  |  '
                                # Units on stock
                                + row[2] + '  |  ' 
                                # Price
                                + row[4] + '  ' + row[3] 
                                + '  |  \n'
                            )    
        except:
            print('Waiting for inventory_items table creation...\n')  
        connection.close()
        del connection, sqlite3    
        # Give data  
        return table
