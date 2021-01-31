#ifndef Item
#define ItemHpp 0
#include <string>
    class Item{
        public:
            Item();
            std::string GetName();
            void SetName(std::string);
        protected:
            std::string Name; 
        private:
    };

#endif