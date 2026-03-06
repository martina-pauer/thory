pub struct Tables
{
    // Atributes
    priv table : &str;
    priv option : &str;
    priv row : [&str; 3];
    priv size : [&str; 3];
    priv ins_container : (&str);
    priv outs_container : (&str);
    priv entries : u16;
    priv changes : u8;
}
// Methods
impl Tables
{
    pub Tables(&self, tab : &str, window_size : [&str; 3])
    {
       // Init conf for dash  
        self.table = tab;
        self.option = "";
        self.row = ["", "", ""];
        self.changes = 0;
        self.entries = 3;
      // Create window of that size
        self.size = window_size;
    }

    pub get_table(&self) -> &str
    {
        return self.table;
    }

    pub get_row(&self) -> [&str; 3]
    {
        return self.row;
    }

    pub get_option(&self) -> &str
    {
        return self.option;
    }

    pub get_changes(&self) -> u8
    {
        return self.changes;
    }

    pub get_entries(&self) -> u16
    {
        return self.entries;
    }

    pub set_inputs(&self, list : &str)
    {
        for input in list
        {
            // Add input to ins_container
            self.ins_container.push(input);
        }

        self.entries = list.len();
    }

    pub run(&self)
    {
        // Create interface
        slint :: slint!
        {
            export component Dash
            {
                inherits Window
                {
                   // Add multiple inputs 
                    for entry in self.ins_container
                    {
                        Text
                        {
                            text: entry;
                            color: blue;
                        }
                        Entry
                        {
                        }
                    }
                    // Add sender button
                    Button
                    {
                        label: "Send";
                    }
                    // Show table with results
                    Text
                    {
                        text: self.table;
                        color: black;
                    }
                }
            }
        }    
    }

    pub parametric_input(&self, paramaters : (&str), property_name : &str)
    {
        // Selection option menu input
    }

    pub on_option_changed(&self)
    {
        // Load new option from the menu
    }

    pub update_table(&self)
    {
        // Update table
        self.table = format!("{}\n", self.table);
        for input in self.row
        {
            self.table = format!("{}\t{}", self.table, input)
        }
    }

    pub send_data(&self)
    {
        // When get all the entries changed then update table and refresh interface
        if (self.changes == self.entries)
        {
            self.update_table()
        }
        else
        {
            // Restart changes
            self.changes = 0;
        }
    }
}