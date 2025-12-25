class Money
{
    public:
        Money(std :: string cur, float price)
        {
            this -> currency = cur;
            this -> amount = price;
        }
    private:
        std :: string currency;    
};

class Good
{
    public:
        Good(std :: string naming, Money price)
        {
            this -> name = naming;
            this -> price = {price.currency price.amount};
            this -> count = 1;
        }

        void calc_price()
        {
        }

        void convert(float equivalence, std :: string currency)
        {
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