import langs
from flask import Flask
from flask import request, render_template_string
import os

web = Flask(__name__)         

def text_content(path: str) -> str:
     '''
        Give content of a file entire
        only text without escape chars
     '''
     content = ''
     
     for line in open(path, 'r').readlines():
        content += line.replace('\n', '')

     return content   
# Define thory web logic in Flask
class Tables():
    def __init__(self, tab: str):
        '''
            Make easier GTK window with tables to
            show data, a very common kind of
            programs for enterprises:

            Tables.table, text for the table

            Tables.option, text with selected option from parametric input
            
            Tables.row, list with the last input has a length of Tables.entries as max

            Tables.external, external function for cleaner and better envs
            
            Tables.entries, number of input for the interface
        '''
        # Object properties
        self.table: str = tab

        self.row: list[str] = []

        self.option: str = ''
        
        self.entries: int = 4

        self.external: None = int(0)

    @web.route('/sended')   
    def get_inputs(self):
        '''
            Get forms values from cookies
            using flask
        '''
        cookie = request.cookies.get('thory').split(',')
        # Update currency name
        self.option = cookie[2]
        # Delete data that don't need now
        cookie.pop(2)
        # Get values from imputs excluding currency name
        for input_data in cookie:
            # Get sended by the page and add to row data
            self.row.append(input_data)
        return render_template_string(text_content('index.html'), result = '')

    @web.route('/')                
    def last_outputs(self, outputs: list[str]):
        '''
            Give text to display
            in the end send to 
            the web page using flask
        '''
        self.run()
        
        content = list(text_content('index.html'))

        counter = 1
         
        for output in outputs:
            # Insert from last label to first label
            content.insert((content.index('</label>') - counter), f'<h1>{output}</h1>')
            counter += 1
        # Insert inside <table> tag
        content.insert((content.index('</table>') - 1), self.table)
            
        return content.__str__()
                     
    def update(self):
        '''
            Send data and update web, show result
        '''
        # Get the last inputs from the form
        self.get_inputs()
        # Make the table output
        text = ''
        # Get all the input and format from the row list
        for data in self.row:
            # Add multiple dash as seperator on each row as chars as the first row
            text += f'|\t{data}\t'
        # Update table with new data
        self.table += f'\n{"-" * (self.row_length + text.__len__())}\n{text}|\n'
        del text
        
    def send_data(self):
            '''
                Event when the data are loaded
                all and the button is pressed
                for don't show weird text by
                missed data not written yet.
            '''        
            # Update view for show the result and save
            self.external()
            # Restart for load more products
            self.row: list[str] = []

            self.get_inputs()
        
    def run(self):
         '''
            Show the current graphical
            interface
         '''
         # Send data to page with response JSON
         os.system(f'flask {__name__} --app run')