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
    updater = open(file_name, 'w')
    
    content: list[list[str]] = get_from_csv(file_name)
    
    row: list[list[str]] = content[row_index]

    text: str = ''
    
    for values in content:
        if values == row:
            values[column_index] = values[column_index].replace(values[column_index], value)
        text += values

    updater.write(text)
    del content, row, text
    updater.close()
    del updater
# Define updates for currencies
data_file: str = 'data/currencies_to_ars.csv'
# From line 2 to last currency row
currency_value: int = 1
# Dollars
update_column_csv(data_file, currency_value, 2, 1364.50)
# Pounds
update_column_csv(data_file, currency_value, 3, 1851.90)
# Euros
update_column_csv(data_file, currency_value, 4, 1610.93)
del data_file, currency_value