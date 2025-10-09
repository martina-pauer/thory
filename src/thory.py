#!/usr/bin/python3
from manager import Tables
import inventhory

stock = inventhory.Inventory()
# Example until know how add products to the table from the inputs
shirt = inventhory.Good('T-Shirt')
shirt.count = 3
shirt.price[1] *= 3

pants = inventhory.Good('Jeans')
pants.count = (shirt.count * 2)
pants.price[1] = (shirt.price / 2)

watch = inventhory.Good('Watches')
watch.count = 2

for product in [shirt, pants, watch]:
    stock.add(product)
    stock.update()
# Main code    
app = Tables(stock.save(), (300, 300))
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
    stock.calc_price()[0],
    stock.calc_price()[1]
)
# Customize with own style
#app.get_style('gtk_theme.css')
# Show the interface when get all
app.run()