#!/usr/bin/python3

# Check is the device has internet connection
# for update currencies values in CSV files
# from online sources.
import os

def get_from_csv(file_name: str) -> list[list[str]]:
    '''
        Give the list of rows in Comma Separated Values 
        with each values row as lists within list.
    '''
    file_handler = open(file_name, 'r')
    
    rows: list[list[str]] = []

    for row in file_handler.readlines():
        rows.append(row.split(', '))

    file_handler.close()
    
    del file_handler

    return rows

def  update_column_csv(file_name: str, column_index: int, row_index: int, value: str):
    '''
        Update value in column in specific row
        in CSV file.
    '''
    content: list[list[str]] = get_from_csv(file_name)
    
    row: list[list[str]] = content[row_index]

    text: str = ''
    
    for values in content:
        if values == row:
            values[column_index] = values[column_index].replace(values[column_index], value)
        for column in range(0, values.__len__() - 1):
            # Format data as CSV output
            text += f'{values[column]}, '
        # Add last column to the text
        text += values[values.__len__() - 1]        
    # After get the content start writing because empty the file before of make this    
    updater = open(file_name, 'w')
    updater.write(text)
    del content, row, text
    updater.close()
    del updater
# Define updates for currencies
data_file: str = 'data/currencies_to_ars.csv'
# From line 2 to last currency row
currency_value: int = 0
# Only could this part when the network is working (use ping for check it when all is ok return 0 status)
if os.system('ping -c1 8.8.8.8') == 0:
    # When the wifi connections is checked get conversions from web sources
    # Dollars
    update_column_csv(data_file, currency_value, 1, '1364.50')
    # Pounds
    update_column_csv(data_file, currency_value, 2, '1851.90')
    # Euros
    update_column_csv(data_file, currency_value, 3, '1610.93')
else:
    print('\t\nThe Connection To Internet Aren\'t Available.\n')
del os, data_file, currency_value