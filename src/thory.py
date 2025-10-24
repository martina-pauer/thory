#!/usr/bin/python3
from manager import Tables
import inventhory

def storage():
        '''
                Storage in database the
                inputs
        '''
        # Define object from the row
        if app.row.__len__() == app.entries and not app.row.__contains__('0') and not app.row.__contains__(''):
           # Only Storage When all the entries are complete    
                product = inventhory.Good(app.row[0])
                product.price = ('ARS', float(app.row[2]))
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
        ['ARS', 'USD', '€', '¥'],
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