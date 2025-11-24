import traslator
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk
# Define Specific software traslations
tra = traslator.Traslator()
# Spanish
tra.add_traslation  (
                        'es', 'Stock', 
                        'Inventario'
                    )

tra.add_traslation  (
                        'es', 'Product Name',
                        'producto'     
                    )

tra.add_traslation  (
                        'es', 'Units In Stock',
                        'Unidades En Inventario'
                    )  

tra.add_traslation    (
                    'es', 'Send',
                    'Enviar'
                )

tra.add_traslation    (
                    'es', 'Price',
                    'Precio'
                ) 

tra.add_traslation    (
                    'es', 'Date', 
                    'Fecha'
                )

tra.add_traslation    (
                    'es', 'Units',
                    'Unidades'
                )   
# French
tra.add_traslation  (
                        'fr', 'Stock', 
                        'Inventaire'
                    )

tra.add_traslation  (
                        'fr', 'Product Name',
                        'Produit'     
                    )

tra.add_traslation  (
                        'fr', 'Units In Stock',
                        'Unités En Inventaire'
                    )  

tra.add_traslation    (
                    'fr', 'Send',
                    'Envoyer'
                )

tra.add_traslation (
                    'fr', 'Price',
                    'Prix'
                ) 

tra.add_traslation    (
                    'fr', 'Date', 
                    'Date'
                )

tra.add_traslation    (
                    'fr', 'Units',
                    'Unités'
                )   
# Deutsch (German)
tra.add_traslation  (
                        'de', 'Stock', 
                        'Inventar'
                    )

tra.add_traslation  (
                        'de', 'Product Name',
                        'Produkt'     
                    )

tra.add_traslation  (
                        'de', 'Units In Stock',
                        'Einheiten Im Bestand'
                    )  

tra.add_traslation    (
                    'de', 'Send',
                    'Schicken'
                )

tra.add_traslation    (
                    'de', 'Price',
                    'Preis'
                ) 

tra.add_traslation    (
                    'de', 'Date', 
                    'Datum'
                )

tra.add_traslation   (
                    'de', 'Units',
                    'Einheiten'
                ) 
# Italian
tra.add_traslation  (
                        'it', 'Stock', 
                        'Inventario'
                    )

tra.add_traslation  (
                        'it', 'Product Name',
                        'prodotto'     
                    )

tra.add_traslation  (
                        'it', 'Units In Stock',
                        "Unità Nell' inventario"
                    )  

tra.add_traslation    (
                    'it', 'Send',
                    'Inviare'
                )

tra.add_traslation    (
                    'it', 'Price',
                    'Prezzo'
                ) 

tra.add_traslation    (
                        'it', 'Date', 
                        'Data'
                    )

tra.add_traslation   (
                    'it', 'Units',
                    'Unità'
                ) 
# Define reusable graphics
class Tables(Gtk.Window):
    def __init__(self, tab: str, window_size: tuple[int, int]):
        '''
            Make easier GTK window with tables to
            show data, a very common kind of
            programs for enterprises:

            Tables.table, text for the table

            Tables.option, text with selected option from parametric input
            
            Tables.ins_container, block for inputs

            Tables.outs_container, block for outputs

            Tables.row, list with the last input has a length of Tables.entries as max

            Tables.row_length, count of characters of first row

            Tables.entries, number of input for the interface

            Tables.changes, number of how much the input text has chaanged

            Table.external, external func when get all the inputs
        '''
        # Set title, width in pixels and height in pixels
        super().__init__(title = 'Stock')
        self.set_size_request(window_size[0], window_size[1])
        # Object properties
        self.table: str = tab

        self.row: list[str] = []

        self.option: str = ''

        self.changes: int = 0
        
        self.entries: int = 0

        self.row_length: int = 0
        
        self.ins_container: Gtk.VBox = Gtk.VBox()
        
        self.outs_container: Gtk.VBox = Gtk.VBox()

        self.external: None = print()
        
    def set_inputs(self, inputs: list[str]):
        '''
            Give different text input
            to the inputs container
        '''
        for input_data in inputs:
            # Create Text input for data
            input_object = Gtk.Entry()
            input_object.set_placeholder_text(tra.traslate(input_data))
            # Count one entry more
            self.entries += 1
            # Give Dafault value to Row for protect from exception
            self.row.append('0') 
            # Update interface everytime the input changes
            input_object.connect('changed', self.update_table)
            # Add object to inputs section: Use recommended method for more widgest
            self.ins_container.pack_start(
                                            input_object, True, 
                                            True, 0
            )
            del input_object
        # Button for prevent table view mistakes
        send = Gtk.Button(label = tra.traslate('Send'))
            
        send.connect('clicked', self.send_data)
        # Add out from the loop for don't put many buttons    
        self.ins_container.pack_start(
                                        send, True,
                                        True, 0
        )
        del send
              
    def last_outputs(self, outputs: list[str]):
        '''
            Give text to display
            in the end
        '''
        for output in outputs:
            self.outs_container.pack_start(
                Gtk.Label(tra.traslate(output)), True,
                True, 0
            )

    def set_columns(self, names: list[str]):
            '''
                Define columns names
            '''
            text: str = ''
            for name in names:
                 text += f'|\t{tra.traslate(name)}\t '
            # Count how much characters has the first and bigest row
            self.row_length = text.__len__()     
            # Add columns names and later table content     
            self.outs_container.pack_start(
                                        Gtk.Label(label = f'{text}|\t\n{self.table}'), True,
                                        True, 0
            ) 
            # Clean memory for optimize and get more for the next process
            del text    
            
    def parametric_input(self, parameters: list[str], property_name: str):
         '''
            Select paramater from menu
            and give it value
         '''  
         # Combo button with menu of options          
         button = Gtk.ComboBoxText()
         button.set_entry_text_column(0)
         button.connect('changed', self.on_option_changed) 
         # Add identifier category and options to select
         for option in parameters:
            button.append_text(option)
         # Use the better for add more than one widget   
         self.ins_container.pack_start(
                                        button, True,
                                        True, 0
         )
         del button
         # Make one Enrty more
         self.entries += 1
         getter = Gtk.Entry()
         getter.set_placeholder_text(tra.traslate(property_name))
         container = Gtk.HBox()
         # Define input event for set the name of product and all the data well
         getter.connect('changed', self.update_table) 
         container.add(getter)
         del getter
         # Use pack_start method for various widgets adding on containers
         self.ins_container.pack_start(
                                        container, True,
                                        True, 0
         )
         del container   

    def update_table(self, widget: Gtk.Entry):
        '''
            Event for input change of
            all the inputs
        '''
        # Save the value from entry for fast up & not lost time asking the same
        entry_text: str = widget.get_text()
        # Get one row when don't pass the entries
        if self.row.__len__() < self.entries:
            self.row.append (
                                entry_text
                            )
        else:
            # Override from the first to the last entry
            self.row[self.changes] = entry_text    
            # Count every change on each entry Only When Is Changing   
            self.changes += 1
        # But not count the extra changes, count only how much entries changes
        if self.changes >= entry_text.__len__():
            self.changes -= (
                                entry_text.__len__() - 1
                            )
        # Free the unned data for get more RAM available
        del entry_text
        # When all the entry change knowing how much add all
        if self.changes == self.entries:
            # Make the table output
            text = ''
            # Get all the input and format from the row list
            for data in self.row:
                # Add multiple dash as seperator on each row as chars as the first row
                text += f'|\t{data}\t'
            # Update table with new data
            self.table += f'\n{"-" * self.row_length}\n{text}|\n'
            del text            
            self.outs_container.pack_start (
                                                Gtk.Label(label = self.table), True,
                                                True, 0
            )
            # Restart for count again after complete info
            self.changes = 0
            
    def send_data(self, sender: Gtk.Button):
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
            self.changes: int = 0
            # Clean all the inputs for load more data
            for entries in self.ins_container.get_children():
                try:
                    # Only apply to text inputs not buttons and menus
                    entries.set_text('')
                except:
                    try:
                    # The Parametric input has a text input apart from the others  
                        if type(entries) != type(Gtk.Button()): 
                            entries.get_children()[0].set_text('')  
                    except:
                        pass

    def on_option_changed(self, menu: Gtk.ComboBoxText):
        '''
            Get the selected option
            from List Button (ComboBoxText)
        '''
        self.option = menu.get_active_text()
        # Select from the last Entry inside other container the text to add
        self.row.append(self.ins_container.get_children()[self.ins_container.__len__() - 2].get_children()[0].get_text())
        
    def get_style(self, css_filename: str):
        '''
            Give custom style from
            CSS file
        '''    
        theme = Gtk.CssProvider()

        content = ''

        with open(css_filename, 'rb') as data:
            content = data.read()

        theme.load_from_data(content)

        context = Gtk.StyleContext()

        viewer = Gdk.Screen()

        context.add_provider_for_screen (
                                            viewer.get_default(),
                                            theme,
                                            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
                                        )    

    def run(self):
         '''
            Show the current graphical
            interface
         '''
         self.connect('delete-event', Gtk.main_quit)
         try:
            # Add one container inside of other for get all the view
            self.ins_container.pack_start(
                                            self.outs_container, True,
                                            True, 0
            )
            # Gtk.Window only have add method for add containers
            self.add(self.ins_container)
            self.show_all()
            Gtk.main()
         except:
            self.close()   