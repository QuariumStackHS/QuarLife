#include "include/SDL.h"
#include <iostream>
sdf
//using namespace std;v
//#pragma startup Initialize
//#pragma exit Post
void Post(){
    std::cout<<"SDL Quit"<<std::endl;
    SDL_Quit();
}
void Initialize(){
    if (SDL_Init(SDL_INIT_EVERYTHING)==0){
        std::cout<<"SDL Initialized"<<std::endl;
    }
    else{
        std::cout<<"Error SDL Could not be Initialized"<<std::endl;
    }
    //SDL_SetVideoMode(1920, 1080, 0);


}
int main(int argc,char** argv){
    Initialize();
    std::cout<<"Main"<<std::endl;
    Post();
return 0;

}