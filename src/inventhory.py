class Good():
    '''
        Represents the inventory good
        with name, available units and
        price:

            Good.name -> str, default class constructor arg
        
            Godd.price -> tuple[str, float], default ARS 1000.00

            Good.count -> int, default 1 unit available
    '''
    def __init__(self, name: str):
        
        self.name: str = name        

        self.price: tuple[str, float] = ('ARS', 1000.00)

        self.count: int = 1
        
    def calc_price(self) -> tuple[str, float]:
        '''    
            calc the total price for
            this good only (unit times the price)
        '''
        return  (
                # Mantain the same currency for be predictible
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

    def save(self):
        '''
            Save the info on the inventory
            using a database scheme:

                first level, inventories database
                second level, this inventory database
                third level, each good info tables
        '''
        consult = open('info.sql', 'a')
        # Make database for all the inventories
        consult.write('CREATE DATABASE inventories;')
        # Do table for this invenetorie in particular
        consult.write(f'CREATE TABLE inventory_{(self.items[0].name + self.items[1].name).replace(' ', '_')} (good_name varchar(255), available_units int, price FLOAT(6, 2);')
        # Insert values from this inventory        
        consult.close()
        del consult
        # use 'info.sql' file for build database
        # remove file by security
        import os
        os.remove('info.sql')
        del os # END OS LIFECYCLE BY SECURITY