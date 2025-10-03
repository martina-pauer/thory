import gi
gi.require_version('Gtk', '3.0')
import Gtk
import Gdk

class Tables(Gtk.window):
    def __init__(self, tab: str, window_size: tuple[int, int]):
        '''
            Make easier GTK window with tables to
            show data, a very common kind of
            programs for enterprises:

            Tables.table, text for the table

            Tables.ins_container, block for inputs

            Tables.outs_container, block for outputs
        '''
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
        pass

    def run(self):
         '''
            Show the current graphical
            interface
         '''
         pass