import langs
         
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
        
    def get_inputs(self):
        '''
            Get forms values from JSON
            using flask
        '''
        #######################################################
        for input_data in data.keys():
            # Get JSON sended by the page and add to row data
            self.row.append(data[input_data])
            # Update interface everytime the input changes sending reponse JSON
            ####################################################################
             
    def last_outputs(self, outputs: list[str]):
        '''
            Give text to display
            in the end send JSON to
            the web page using flask
        '''
        for output in outputs:
            pass
            
    def parametric_input(self):
         '''
            Select paramater from menu
            and give it value using Flask
         '''  
         # Get option from the form
         ########################################
         self.option = data["thory-currency"]
         

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
        # Send JSON for update web table and reload
        ###############################################
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
        
    def run(self):
         '''
            Show the current graphical
            interface
         '''
         # Send data to page with response JSON
         pass