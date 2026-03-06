#include <gtk/gtk.h>
#include "lang.hpp"

class Tables
{
    public:
        Tables(string tab, int[2] window_size)
        {
           // Start basic conf for simple 3 inputs with text table dash 
            this -> table = tab;
            this -> option = "";
           // Number of input changed from 0 to entries number 
            this -> changes = 0;
          // Storage in next row item until get entries number before restart the list  
            this -> entries = 3;
            this -> row = {"", "", ""};
        }

        void set_name(std :: string software)
        {
           // Give title to the software of this way is more flexible the window title 
            this -> software_name = software;
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

        int get_gtk_status()
        {
            return this -> status;
        }

        void set_inputs(GtkWidget*[] list)
        {
            // Set the Gtk entries for add to input containes
            for (int entry = 1; entry <= (this -> entries); entry++)
            {
                // Add Gtk entry from list to input container
                this -> ins_container.add(list[entry]);
            }
            // Add Output container to input container
            gtk_container_add(GTK_CONTAINER (this -> ins_container), this -> outs_container)
            // Add input container to the window
            gtk_container_add(GTK_CONTAINER (window), this -> ins_container);
        }

        void parametric_input(std :: string[] parameters, std :: string property_name)
        {
            // Create selection input menu
        }

        static void update_table(GtkWidget *input, gpointer data)
        {
          // Updater event for add new data 
            if ((this -> changes) < (this -> entries))
            {
            //?    
                this -> row[this -> changes] = input.get_text();
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
            GtkWidget *label = gtk_new_label(this -> table);
            gtk_container_add(GTK_CONTAINER (this -> outs_container), label);
            // Refresh interface
            this -> run();
        }

        static void send_data(GtkWidget *sender, gpointer data)
        {
            // Load data and refresh interface when the button is pressed
            this -> update_table(sender, data);
        }

        static void on_option_changed(GtkWidget *menu, gpointer data)
        {
            // Load text from the input that has changed the option form selection
            //?
            this -> option = menu.get_text()
        }

        static void run(GtkApplication *app, gpointer data)
        {
            // Create Gtk containers 
            this -> ins_container = gtk_button_box_new(GTK_ORIENTATION_VERTICAL);
            this -> outs_container = gtk_button_box_new(GTK_ORIENTATION_VERTICAL); 
         // Create window with that size
            this -> window = gtk_application_new(app);
            gtk_window_set_title (GTK_WINDOW (this -> window), this -> software_name)
            gtk_window_set_deafault_size (GTK_WINDOW (this -> window), window_size[0], window_size[1]);
         // Connect updater event to the button
            GtkWidget *send = gtk_button_new_with_label(translation.translate("Send"));
            g_signal_connect(send, "clicked", G_CALLBACK (this -> send_data), NULL);
         // Add button to the outs_continer
            gtk_container_add(GTK_CONTAINER (this -> outs_container), send);   
        // Show the interface
            gtk_widget_show_all (this -> window);
            GtkApplication *AppID = gtk_application_new("org.gtk.app", g_application_flags_none);
            this -> status = g_application_run(g_application(app), NULL, NULL);
            g_object_unref(app);
        }
    private:
        std :: string table;
        std :: string option;
        std :: string[] row;
        std :: string software_name;
        int status;
        int changes;
        int entries;
        GtkWidget *ins_container;
        GtkWidget *outs_container;
        GtkWidget *window;
};