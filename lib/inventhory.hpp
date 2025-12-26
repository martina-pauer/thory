class Money
{
    public:
        Money(std :: string cur, float price)
        {
            this -> currency = cur;
            this -> amount = price;
        }

        float get_amount()
        {
            return this -> amount;
        }

        std :: string get_currency()
        {
            return this -> currency;
        }    
    private:
        std :: string currency; 
        float amount;   
};

class Good
{
    public:
        Good(std :: string naming, Money price_object)
        {
            this -> name = naming;
            this -> price = price_object;
            this -> count = 1;
        }

        void set_count(int recount)
        {
            // Set new count of available units in stock
            this -> count = recount;
        }
            
        void calc_price()
        {
            this -> price = Money(this -> price.get_currency(), this -> price.get_amount() * this -> count);
        }

        void convert(float equivalence, std :: string currency)
        {
            this -> price = Money(currency, this -> price.get_amount() * equivalence);
        }   

        std :: string get_name()
        {
            return this -> name;
        }     

        Money get_price()
        {
            return this -> price;
        }

        int get_count()
        {
            return this -> count;
        }     
    private:
        std :: string name;
        Money price;
        int count;
};

class Inventhory
{
    public:
        Inventhory()
        {
            this -> items = {};
            this -> goods = 1;
            this -> count = 0;
        }
        
    private:
        Good[] items;
        int goods;
        int count;

};