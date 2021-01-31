#include "Common/Item.h"

Item::Item(){

}
std::string Item::GetName(){
    return this->Name;
}
void Item::SetName(std::string name){
    this->Name=name;
}