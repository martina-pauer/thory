#!/usr/bin/python3
from manager import Tables
import inventhory

# External to function object for reinput many times
stock = inventhory.Inventory()

def storage():
        '''
                Storage in database the
                inputs
        ''' 
        product = inventhory.Good(app.row[0])
        # When the price is ARSED (pesificado) leave of that way
        product.price = ['ARS', float(app.row[3])]
        # Only make convertion when the selected currency is diff to ARS
        if app.option == 'USD':
        # Convert from Law Dollar to ARS
                product.convert(1475.00, 'ARS')
        elif app.option == '€':
                # Only need change the saved amount for don't search the same data
                product.convert(1844.55, 'ARS')
        elif app.option == '£':
                # Pounds Value  
               product.convert(2026.65, 'ARS')         
        # When select one of defined curreuncies different to ARS make converrtion                     
        product.count = int(app.row[1])
        # Storage in database
        stock.add(product)
        app.table = stock.save()
        # Show total price in external object with stock
        app.last_outputs(
                                [
                                        # Show the total price on inventory before add table
                                        f'Total Value: {stock.calc_price()[1]} {stock.calc_price()[0]}'
                                ]
                        )
        # Update inetrface
        app.update()
# Main code    
app = Tables('')
app.parametric_input(
        ['ARS', 'USD', '€', '£'],
        'Price'    
)

# External func for update
app.external = storage
# Show the interface when get all
app.run()