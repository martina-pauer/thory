pub struct Good
{ 
    // Atributes
    name: &str,
    price: (&str, f32),
    count: u32
}

pub struct Inventhory
{
    items: Vec<Good>
    goods: u32,
    count: u32
}
// Methods
impl Good
{
    pub fn calc_price(&self) -> (&str, f32)
    {
      // Calc price by mult unitary price and unit in stock  
        self.price.1 = (self.price.1 * self.count);
    // Give the result as tuple 'currency' and 'price' only type multi-type
        return self.price
    }

    pub fn convert(&self, equiv:f32, cur:&str)
    {
      // Made the change from one currency to other for get equivalent price  
        self.price.1 = self.price.1 * equiv;
        self.price.2 = cur;
    }

    pub fn get_name(&self) -> &str
    {
        return self.name;
    }

    pub fn get_price(&self) -> (&str, f32)
    {
        return self.price;
    }

    pub fn get_count(&self) -> u32
    {
        return self.count;
    }
}

impl Inventhory
{
    pub fn update(&self)
    {
        // Check that all properties are up to date
        if (self.count < self.items.length)
        {
            let mut before : Good = self.items[0];

            let mut index_first : u32 = 1;
            let mut index_second : u32 = 1;

            while (index_first < self.items.len())
            {
                // Compare the first with each elemnts in the list
                    while (index_second < self.items.len())
                    {
                        if before != self.items[index_second]
                        {
                          // Count only the repeats of each product in the list  
                            self.goods = self.goods + 1;
                        }
                        index_second = index_second + 1;
                    }    
                    before = self.items[index_first]
            }
        }
        // Count the items in total not matter repeat
        self.count = self.items.len();
    }

    pub fn add(&self, product : Good)
    {
        self.items.push(product);
        self.update();
    }

    pub fn calc_price(&self) -> (&str, f32)
    {
        for item in self.items
        {
            item.calc_price();
        }   
        return self.get_price();
    }

    pub fn save(&self) -> &str
    {
       // Storage data in database and give table ass text 
        let mut table : &str = "";
      // SQL requests  
        let consult : String = String :: from("CREATE TABLE " + langs.traslations.traslate("inventory_items") + "(" + langs.traslations.traslate("Moment") + " timestamp, " + langs.traslations.traslate("Good_Name") + " varchar(255), " + langs.traslations.traslate("Available_Units")} + " int, " + langs.traslations.traslate("Price") + " DECIMAL(6, 2), " + langs.traslations.traslate("Currency") + " varchar(3), " + langs.traslations.traslate("Total_ARS_Price") + " DECIMAL(6, 2));");
     // Run SQL commands from the reuqests   
     // insert values
        for item in self.items
        {   
            let insertion : String = String :: from("INSERT INTO " + langs.traslations.traslate('inventory_items') + "(" + langs.traslations.traslate('Moment') + ", " + langs.traslations.traslate('Good_Name') + ", " + langs.traslations.traslate('Available_Units') + ", " + langs.traslations.traslate('Price') + ", " + langs.traslations.traslate('Currency') + ", " + langs.traslations.traslate('Total_ARS_Price') + ") VALUES (datetime('now', 'localtime'), '" + item.name + "', " + item.count + ", " + item.price[1] + ", '" + item.price[0] + "', " + self.calc_price()[1] + ")");
            // Make insertion to SQL database
        }    
        return table;
    }

    pub fn get_items(&self) -> Vec<Good>
    {
        return self.items;
    }

    pub fn get_goods(&self) -> u32
    {
        return self.goods;
    }

    pub fn get_count(&self) -> u32
    {
        return self.count;
    }
}