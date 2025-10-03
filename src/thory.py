#!/usr/bin/python3
from manager import Tables
import inventhory

app = Tables(inventhory.Inventory, (300, 300))
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
# Define the text to show
app.last_outputs(
    # Show the price of all the stock
    inventhory.Inventory.calc_price()[0],
    inventhory.Inventory.calc_price()[1]
)
# Customize with own style
app.get_style('gtk_theme.css')
# Show the interface when get all
app.run()