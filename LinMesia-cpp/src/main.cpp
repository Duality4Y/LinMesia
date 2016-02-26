#include <stdio.h>
#include <SDL.h>

#include "MidiFile.h"

const int SCREEN_WIDTH = 640;
const int SCREEN_HEIGHT = 480;

int main(int argc, char** argv)
{
    SDL_Window* window = NULL;
    SDL_Surface* screenSurface = NULL;

    if(SDL_Init(SDL_INIT_VIDEO) < 0)
    {
        printf("SDL could not initialize! SDL_Error: %s\n",
               SDL_GetError());
        return 1;
    }

    window = SDL_CreateWindow("SDL Tutorial", SDL_WINDOWPOS_UNDEFINED,
                              SDL_WINDOWPOS_UNDEFINED, 
                              SCREEN_WIDTH, SCREEN_HEIGHT,
                              SDL_WINDOW_SHOWN);
    if(window == NULL)
    {
        printf("SDL could not create a window. %s\n",
               SDL_GetError());
        return 1;
    }

    screenSurface= SDL_GetWindowSurface(window);
    printf("width: %d\n", screenSurface->w);
    printf("height: %d\n", screenSurface->h);
    SDL_FillRect(screenSurface, NULL, SDL_MapRGB(screenSurface->format, 0xff, 0xff, 0xff));

    SDL_UpdateWindowSurface(window);

    SDL_Delay(2000);

    return 0;
}
