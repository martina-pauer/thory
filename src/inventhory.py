class Good():
    '''
        Represents the inventory good
        with name, available units and
        price:

            Good.name -> str, default class constructor arg
        
            Good.price -> tuple[str, float], default ARS 1000.00

            Good.count -> int, default 1 unit available
    '''
    def __init__(self, name: str):
        
        self.name: str = name        

        self.price: tuple[str, float] = ('ARS', 1000.00)

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
            self.price: tuple[str, float] = (self.price[0].__str__(), float(self.price[1]))
        except:
            print('- Good.price must be a 2 fields tuple text and floating point\n')    
        
    def calc_price(self) -> tuple[str, float]:
        '''    
            calc the total price for
            this good only (unit times the price)
        '''
        return  (
                # Mantain the same currency for be more predictible
                    self.price[0], 
                # Price unit times only with 2 decimals    
                    round(self.count * self.price[1], 2)
                )

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
            for item in range((self.count - 1), self.items.__len__):
                # Compare with the previous goods for new kinds
                for other in range(0, self.count):
                    different = (other.name != self.items[item].name)
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

    def calc_price(self) -> tuple[str, float]:
        '''
            Calc the price making the sum 
            of all goods prices
        '''          
        inventory_price: tuple[str, float] = (self.items[0], 0.00)
        
        for item in self.items:
            # Sum the prices when are in the same currency
            if (inventory_price[0] == item.calc_price()[0]):    
                inventory_price[1] = round(inventory_price[1] + item.calc_price()[1], 2)
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
        consult = open('info.sql', 'a')
        # Do table for this inventory in particular
        # Columns in table: moment, good_name, available_units, price, currency
        consult.write('CREATE TABLE inventory_items (moment timestamp good_name varchar(255), available_units int, price FLOAT(8, 2), currency varchar(3));')
        # Insert values from this inventory        
        for item in self.items:
                item.fix_types()
                consult.write(f"INSERT INTO inventory_items(moment, good_name, available_units, price, currency) VALUES (CURRENT_TIMESTAMP, {item.name}, {item.count}, {item.price[1]}, '{item.price[0]}');")
        consult.close()
        del consult
        # Load from the file and run in sqlite SQL manager
        result: str = self.load('info.sqlite')
        # remove file by security
        import os
        os.remove('info.sqlite')
        del os # END OS LIFECYCLE BY SECURITY
        # Give the table as text to the next process
        return result

    def load(self, file_name: str) -> str:
        '''
            Load SQL files with inventory_item table
            with the columns:
                moment,
                good_name, 
                available_units,
                price,
                currency

            Return the text with the data as table.    
        '''
        data = open(file_name, 'r')    

        import sqlite3
        connection = sqlite3.connect('inventory.db')
        cursor = connection.cursor()
        
        for command in data.readlines():
            command = command.replace('\n', '')
            # Run with sqlite3
            try:
                # Handle exceptions like table already created or similar
                cursor.execute(command)
            except:
                print(f'Mistake in SQL command {command}')    
            connection.commit()
        # Run a select command for make work fetchall method 
        cursor.execute('SELECT * FROM inventory_items;')   
        # Format table as text string
        table: str = ''
        for row in cursor.fetchall():
                # Run one time the fetchall method for add rows
                table += (
                            # Date
                            '|  ' + row[0] + '  |  '
                            # Name of product
                            + row[1] + '  |  '
                            # Units on stock
                            + row[2] + '  |  ' 
                            # Price
                            + row[4] + '  ' + row[3] 
                            + '  |  \n'
                        )    
        connection.close()
        del connection, sqlite3    
        data.close() 
        del data
        # Give data  
        return table