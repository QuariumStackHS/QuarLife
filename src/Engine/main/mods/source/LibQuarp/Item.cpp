#include "mods/LibQuarp/Item.h"
#include "include/SDL.h"
#include "include/SDL_image.h"
Item::Item(){

}
std::string Item::GetName(){
    return this->Name;
}
void Item::SetName(std::string name){
    this->Name=name;
}