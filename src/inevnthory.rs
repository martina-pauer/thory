pub struct Good
{ 
    // Atributes
    name: &str,
    price: Vec<&str, f32>,
    count: u32
}
// Methods
impl Good
{
    pub fn calc_price(&self)
    {
        self.price[1] *= (self.price[1] * self.count);
    }
}