#include <string>
#include <sqlapi.h>
#include "lang.hpp"

class Money
{
    private:
        std :: string currency; 
        float amount;    
    public:
        Money()
        {
            this -> currency = "ARS";
            this -> amount = 3000.00;
        }

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
};

class Good
{
    private:
        std :: string name;
        Money price;
        int count;    
    public:
        Good()
        {
            // Use constructor overload only for turn this into a type for clone objects into a list
            this -> count = 1;
            this -> name = "some";
            this -> price = Money();
        }

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
};

class Inventhory
{
    private:
        Good[] items;
        int goods;
        int count;
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
            std :: string consult = "CREATE TABLE " + langs.traslations.traslate("inventory_items") + "(" + langs.traslations.traslate("Moment") + " timestamp, " + langs.traslations.traslate("Good_Name") + " varchar(255), " + langs.traslations.traslate("Available_Units")} + " int, " + langs.traslations.traslate("Price") + " DECIMAL(6, 2), " + langs.traslations.traslate("Currency") + " varchar(3), " + langs.traslations.traslate("Total_ARS_Price") + " DECIMAL(6, 2));";
            // Define connection to database and commands
            SAConnection connection;
            SACommand cmd;
            // Connect to database
            connection.Connect("test", "tester" "tester", SA_oracle_Client);
            cmd.SetCommandText(consult);
            // Make changes in database
            cmd.execute();
            connection.Commit();
            // Add each product from inventory to SQL database
            for (int good_index = 0; good_index < sizeof(this -> items) / sizeof(this -> items[0]); good_index++)
            {
                Good item = this -> items[good_index];
                std :: string insertion = "INSERT INTO " + langs.traslations.traslate('inventory_items') + "(" + langs.traslations.traslate('Moment') + ", " + langs.traslations.traslate('Good_Name') + ", " + langs.traslations.traslate('Available_Units') + ", " + langs.traslations.traslate('Price') + ", " + langs.traslations.traslate('Currency') + ", " + langs.traslations.traslate('Total_ARS_Price') + ") VALUES (datetime('now', 'localtime'), '" + item.name + "', " + item.count + ", " + item.price[1] + ", '" + item.price[0] + "', " + this -> calc_price()[1] + ")";
                cmd.SetCommandText(insertion);
                cmd.execute();
                connection.Commit();
            }
            std :: string result = "";
            return result;
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
};