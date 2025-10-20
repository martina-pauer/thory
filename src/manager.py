import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk

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
        '''
        # Set title, width in pixels and height in pixels
        super().__init__(title = 'Stock')
        self.set_size_request(window_size[0], window_size[1])
        # Object properties
        self.table: str = tab

        self.option: str = ''
        
        self.ins_container: Gtk.VBox = Gtk.VBox()

        self.outs_container: Gtk.HBox = Gtk.HBox()
        
    def set_inputs(self, inputs: list[str]):
        '''
            Give different text input
            to the inputs container
        '''
        for input_data in inputs:
            # Create Text input for data
            input_object = Gtk.Entry()
            input_object.set_placeholder_text(input_data)
            # Update interface everytime the input changes
            input_object.connect('changed', self.run)
            # Add object to inputs section: Use recommended method for more widgest
            self.ins_container.pack_start(
                                            input_object, True, 
                                            True, 0
            )
            del input_object
            
    def last_outputs(self, outputs: list[str]):
        '''
            Give text to display
            in the end
        '''
        for output in outputs:
            self.outs_container.pack_start(
                Gtk.Label(output), True,
                True, 0
            )

    def set_columns(self, names: list[str]):
            '''
                Define columns names
            '''
            text: str = ''
            for name in names:
                 text += f'|\t{name}\t '
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
         button.connect('changed', self.on_currency_changed) 
         # Add identifier category and options to select
         for option in parameters:
            button.append_text(option)
         # Use the better for add more than one widget   
         self.ins_container.pack_start(
                                        button, True,
                                        True, 0
         )
         del button
         getter = Gtk.Entry()
         getter.set_placeholder_text(property_name)
         container = Gtk.HBox()
         container.add(getter)
         del getter
         # Use pack_start method for various widgets adding on containers
         self.ins_container.pack_start(
                                        container, True,
                                        True, 0
         )
         del container   

    def on_currency_changed(self, menu: Gtk.ComboBoxText):
        '''
            Get the selected option
            from List Button (ComboBoxText)
        '''
        self.option = menu.get_active_text()
        
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

        context = Gtk.StyleContex()

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
            self.outs_container.pack_start(
                                            self.ins_container, True,
                                            True, 0
            )
            # Gtk.Window only have add method for add containers
            self.add(self.outs_container)
            self.show_all()
            Gtk.main()
         except:
            self.close()   