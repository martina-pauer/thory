#include <gtk/gtk.h>

class Tables
{
    public:
        Tables(string tab, int[][] window_size)
        {
           // Start basic conf for simple 3 inputs with text table dash 
            this -> table = tab;
            this -> option = "";
           // Number of input changed from 0 to entries number 
            this -> changes = 0;
          // Storage in next row item until get entries number before restart the list  
            this -> entries = 3;
            this -> row = {"", "", ""};
         // Create Gtk containers 
         //////////////////////////////////////////////
            this -> ins_container = ;
        /////////////////////////////////////////////    
            this -> outs_container = ; 
         // Create window with that size
         // Connect updater event to the button
        }

        std :: string get_table()
        {
            // Return the table with inventhory
            return this -> table;
        }

        std :: string[] get_row()
        {
            // Get the inputs from entries
            return this -> row;
        }

        std :: string get_option()
        {
            // Get selected option from form selection menu input text
            return this -> option;
        }

        int get_changes()
        {
            // Get how much input changes
            return this -> changes;
        }

        int get_entries()
        {
            // Get how much entries are
            return this -> entries;
        }

        void set_inputs(list)
        {
            // Set the Gtk entries for add to input containes
            for (int entry = 1; entry <= (this -> entries); entry++)
            {
                // Add Gtk entry from list to input container
                this -> ins_container.add(list[entry]);
            }
            // Add Output container to input container
            /////////////////////////////////////////////////////
            // Add input container to the window
            ///////////////////////////////////////////////////////
            // Add Send button to the window
            /////////////////////////////////////////////////////
        }

        void parametric_input(std :: string[] parameters, std :: string property_name)
        {
            // Create selection input menu
        }

        void update_table()
        {
          // Updater event for add new data 
            if ((this -> changes) < (this -> entries))
            {
            ////////////////////////////////////////////////////////////////////////    
                this -> row[this -> changes] = ;
            }
            else
            {
                // Restart changes when is greater or equal to all entries
                this -> changes = 0;
            }
            // Add row data to table
            for (int entry = 0; entry < (this -> changes); entry++)
            {
                this -> table = ((this -> table) + "\n" + (this -> row[entry]) + " | ");
            }
            // Add Table to Output containers
            /////////////////////////////////////////////////////////////////////////
            text = ;
            this -> outs_container.add(text);
            // Refresh interface
            this -> run();
        }

        static void send_data(sender)
        {
            // Load data and refresh interface when the button is pressed
            this -> update_table();
        }

        static void on_option_changed(menu)
        {
            // Load text from the input that has changed the option form selection
            //////////////////////////////////////////////////////////////////////////
        }

        void run()
        {
            // Show the interface
            //////////////////////////////////////////////////////////////////////////
        }
    private:
        std :: string table;
        std :: string option;
        std :: string[] row;
        int changes;
        int entries;
        /////////////////////////////////////////////////////////////////////////////
        ins_container;
        ////////////////////////////////////////////////////////////////////////////
        outs_container;
};