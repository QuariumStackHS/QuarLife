#include "include/SDL.h"
#include "include/SDL_image.h"
#include <iostream>

//using namespace std;v
//#pragma startup Initialize
//#pragma exit Post
#define ResourcePath "resource/"
class GameEngine
{
public:
    GameEngine()
    {

        std::cout << "New Quarium Engine Initialised" << std::endl;
        //return NULL;
    }
    int register_items()
    {
        return 0;
    }
    int draw_map()
    {

        /*
        draw frames*/

        return 0;
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
    SDL_Renderer *renderer = NULL;
    void Post()
    {
        std::cout << "SDL Quit" << std::endl;
        SDL_Quit();
    }
    SDL_Texture *loadTexture(std::string path)
    {
        //The final texture
        SDL_Texture *newTexture = NULL;

        //Load image at specified path
        SDL_Surface *loadedSurface = IMG_Load(strcat(ResourcePath,path.c_str());
        if (loadedSurface == NULL)
        {
            printf("Unable to load image %s! SDL_image Error: %s\n", path.c_str(), IMG_GetError());
        }
        else
        {
            //Create texture from surface pixels
            newTexture = SDL_CreateTextureFromSurface(this->renderer, loadedSurface);
            if (newTexture == NULL)
            {
                printf("Unable to create texture from %s! SDL Error: %s\n", path.c_str(), SDL_GetError());
            }

            //Get rid of old loaded surface
            SDL_FreeSurface(loadedSurface);
        }

        return newTexture;
    }
    //initialise Engine
    void Initialize()
    {
        if (SDL_Init(SDL_INIT_VIDEO) == 0)
        {
            std::cout << "SDL Initialized" << std::endl;
        }
        else
        {
            std::cout << "Error SDL Could not be Initialized" << std::endl;
        }
        SDL_Window *screen = SDL_CreateWindow("My Game Window",
                                              SDL_WINDOWPOS_CENTERED,
                                              SDL_WINDOWPOS_CENTERED,
                                              1000, 1000,
                                              SDL_WINDOW_FULLSCREEN);
        SDL_Renderer *renderer = SDL_CreateRenderer(screen, -1,0);

        //SDL_Surface* surface = IMG_Load();
        //loadTexture("Logo.png");
        SDL_SetRenderDrawColor(renderer, 105, 0, 0, 255);
        SDL_RenderClear(renderer);
        SDL_RenderPresent(renderer);
         SDL_Delay(30000);
        //SDL_SetVideoMode(1920, 1080, 0);
    }
};