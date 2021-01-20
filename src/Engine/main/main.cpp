
#include <SDL/SDL.h>
#include <iostream>
//using namespace std;
//#pragma startup Initialize
//#pragma exit Post
void Post(){
    SDL_Quit();
}
void Initialize(){
    if (SDL_Init(SDL_INIT_EVERYTHING)==0){
        std::cout<<"SDL Initialized"<<std::endl;
    }
    else{
        std::cout<<"Error SDL Could not be Initialized"<<std::endl;
    }
    SDL_SetVideoMode(640, 480, 0,SDL_DOUBLEBUF|SDL_FULLSCREEN);


}
int main(int argc,char** argv){
    Initialize();
    std::cout<<"Main"<<std::endl;
    Post();
return 0;

}