#!/usr/bin/python3
from manager import Tables
import inventhory

stock = inventhory.Inventory()
# Example until know how add products to the table from the inputs
shirt = inventhory.Good('T-Shirt')
shirt.count = 3
shirt.price[1] *= 3.00

pants = inventhory.Good('Jeans')
pants.count = (shirt.count * 2)
pants.price[1] = (shirt.price[1] / 2)

watch = inventhory.Good('Watches')
watch.count = 2

for product in [shirt, pants, watch]:
    stock.add(product)
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
# Customize with own style
app.get_style('gtk_theme.css')
# Show the interface when get all
app.run()
# Convert price of products
for product in stock.items:
    app.last_outputs(
        # Show the price of all the stock,
        stock.calc_price()
    )
    if product.price[0] != 'ARS':
        # The convert from lower to greater is 1 divided price for buy one great
        product.convert((1542.41 ** (-1)), app.option)
    # Define object from the row    
    prod = inventhory.Good      (
                                    app.row[0]
                                )
    prod.count = app.row[1]
    prod.price = (product.price[0], app.row[1])
    # Add to stock and storage in database
    stock.add(prod)
    app.table = stock.save()
    # Refresh interface     
    app.show_all()