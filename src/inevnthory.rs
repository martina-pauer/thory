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

    }

    pub fn add(&self)
    {

    }

    pub fn calc_price(&self) -> (&str, f32)
    {
        for item in self.items
        {
            item.calc_price();
        }   
    }

    pub fn save(&self) -> &str
    {
       // Storage data in database and give table ass text 
        let mut table = "";
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