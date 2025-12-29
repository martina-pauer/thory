pub struct Good
{ 
    // Atributes
    name: &str,
    price: Vec<&str, f32>,
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
    pub fn calc_price(&self)
    {
        self.price[1] *= (self.price[1] * self.count);
    }

    pub fn convert(&self, equiv:f32, cur:&str)
    {

    }

    pub fn get_name(&self)
    {

    }

    pub fn get_price(&self)
    {

    }

    pub fn get_count(&self)
    {

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

    pub fn calc_price(&self)
    {

    }

    pub fn save(&self)
    {

    }

    pub fn get_items(&self)
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