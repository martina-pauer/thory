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

            Tables.ins_container, block for inputs

            Tables.outs_container, block for outputs
        '''
        # Set title, width in pixels and height in pixels
        super().__init__(title = 'Stock')
        self.set_size_request(window_size[0], window_size[1])
        # Object properties
        self.table: str = tab
        
        self.ins_container = Gtk.VBox()

        self.outs_container = Gtk.HBox()
        
    def set_inputs(self, inputs: list[str]):
        '''
            Give different text input
            to the inputs container
        '''
        for input_data in inputs:
            self.ins_container.add(
                    Gtk.Entry
                    (
                        label = input_data
                    )
                )
            
    def last_outputs(self, outputs: list):
        '''
            Give text to display
            in the end
        '''
        for output in outputs:
            self.outs_container.add(
                Gtk.Label(output)
            )

    def set_columns(self, names: list[str]):
            '''
                Define columns names
            '''
            for name in names:
                 pass
            
    def parametric_input(self, parameters: list[str], property_name: str):
         '''
            Select paramater from menu
            and give it value
         '''            
         pass   

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
            self.add(self.ins_container)
            self.add(self.outs_container)
            self.show_all()
            Gtk.main()
         except:
            self.close()   