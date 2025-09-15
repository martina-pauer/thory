class Good():
    '''
        Represents the inventory good
        with name, available units and
        price:

            Good.name -> str, default class constructor arg
        
            Godd.price -> tuple[str, float], default ARS 1000.00

            Good.count -> int, default 1 unit available
    '''
    def __init__(self, name):
        
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