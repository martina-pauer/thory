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
            if ((recount >= 1) && (recount <= 2147483647))
            {
                this -> count = recount;
            }
            else
            {
                this -> count = 2;    
            }    
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

        void update()
        {
            // Compare all the items gor counts kinda goods
            Good before = this -> items[0];
            for (int first_element = 1; first_element < sizeof(this -> items) / sizeof(this -> items[0]); first_element++) 
            {
                // Compare the first elements with the next for counts repeats
                for (int second_element = 2; second_element < sizeof(this -> items) / sizeof(this -> items[0]); second_element++)
                {
                    if (before != this -> items[second_element])
                    {
                        this -> goods += 1;
                    }
                }
                before = this -> items[first_element];
            }
        }
        
        void add(Good product)
        {
            this -> items.push_back(product);
        }

        Money[] calc_price()
        {
            Money[] prices = {};

            for (int index = 0; index < sizeof(this -> items) / sizeof(this -> items[0]); index++)
            {
                this -> items[index].calc_price()
            }

            return prices;
        }

        std :: string save()
        {
            // Save in database and get table text
        }

        Good[] get_items()
        {
            return this -> items;
        }

        int get_goods()
        {
            return this -> goods;
        }

        int get_count()
        {
            return this -> count;
        }
    private:
        Good[] items;
        int goods;
        int count;

};