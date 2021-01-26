#include "include/SDL.h"
#include <iostream>

//using namespace std;v
//#pragma startup Initialize
//#pragma exit Post

class GameEngine
{
public:
    void *operator new(size_t size)
    {

        std::cout << "New Quarium Engine Initialised" << std::endl;
    }
    int newIns()
    {

        return 0;
    }
    // main func of Engine, Run the Game with libs in Quarp
    int main()
    {
        Initialize();
        std::cout << "Main" << std::endl;
        Post();
        return 0;
    }

private:
    void Post()
    {
        std::cout << "SDL Quit" << std::endl;
        SDL_Quit();
    }
    //initialise Engine
    void Initialize()
    {
        if (SDL_Init(SDL_INIT_EVERYTHING) == 0)
        {
            std::cout << "SDL Initialized" << std::endl;
        }
        else
        {
            std::cout << "Error SDL Could not be Initialized" << std::endl;
        }
        SDL_Window *screen = SDL_CreateWindow("My Game Window",
                                              SDL_WINDOWPOS_UNDEFINED,
                                              SDL_WINDOWPOS_UNDEFINED,
                                              0, 0,
                                              SDL_WINDOW_FULLSCREEN_DESKTOP);
        SDL_Renderer *renderer = SDL_CreateRenderer(screen, -1, 0);
        //SDL_SetVideoMode(1920, 1080, 0);
    }
};