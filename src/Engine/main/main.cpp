#include "include/SDL.h"
#include <iostream>

//using namespace std;v
//#pragma startup Initialize
//#pragma exit Post
void Post(){
    std::cout<<"SDL Quit"<<std::endl;
    SDL_Quit();
}
//initialise Engine
void Initialize(){
    if (SDL_Init(SDL_INIT_EVERYTHING)==0){
        std::cout<<"SDL Initialized"<<std::endl;
    }
    else{
        std::cout<<"Error SDL Could not be Initialized"<<std::endl;
    }
    SDL_Window *screen = SDL_CreateWindow("My Game Window",
                          SDL_WINDOWPOS_UNDEFINED,
                          SDL_WINDOWPOS_UNDEFINED,
                          640, 480,
                          SDL_WINDOW_FULLSCREEN | SDL_WINDOW_OPENGL);
    //SDL_SetVideoMode(1920, 1080, 0);


}
int main(int argc,char** argv){
    Initialize();
    std::cout<<"Main"<<std::endl;
    Post();
return 0;

}