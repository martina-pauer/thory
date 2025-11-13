#!/usr/bin/python3
from manager import Tables
import inventhory

def storage():
        '''
                Storage in database the
                inputs
        '''
        # Define object from the row
        if app.entries <= (
                                # Discount changes from name input
                                        app.row.__len__() 
                                        + app.ins_container.get_children()[app.ins_container.__len__() - 1].get_children()[0].get_text().__len__() 
                                        + 1
                          ):
           # Only Storage When all the entries are complete witout count the name characters as changes   
                product = inventhory.Good(app.row[2])
                # When the price is ARSED (pesificado) leave of that way
                product.price = ('ARS', float(app.row[3]))
                # Only make convertion when the selected currency is diff to ARS
                if app.option == 'USD':
                        # Convert from Law Dollar to ARS
                        product.convert(1430, 'ARS')
                elif app.option == '€':
                        # Only need change the saved amount for don't search the same data
                        product.convert(1757.80, 'ARS')
                elif app.option == '£':
                        # Pounds Value  
                        product.convert(1964.82, 'ARS')         
                # When select one of defined curreuncies different to ARS make converrtion                     
                product.count = app.row[1]
                # Storage in database
                stock = inventhory.Inventory()
                stock.add(product)
                app.table = stock.save()
                app.show_all()
# Main code    
app = Tables('', (300, 300))
# Define the data getting
app.set_inputs(
        [
            'Product Name',
            'Units In Stock'
        ]
)

app.parametric_input(
        ['ARS', 'USD', '€', '£'],
        'Price'    
)

# Give name to the columns
app.set_columns(
        [
            'Date', 'Name',
            'Units', 'Price'
        ]
)
# Customize with own style
app.get_style('gtk_theme.css')
# External func for update
app.external = storage
# Show the interface when get all
app.run()