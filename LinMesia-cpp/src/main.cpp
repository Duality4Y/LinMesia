#include <SDL.h>

class Game
{
public:
    Game();
    int init();
    void run();
    void quit();
private:
    const int window_width = 800;
    const int window_height = 600;
    char window_title[50] = "LinMesia";
    SDL_Window *window = NULL;
    SDL_Renderer *renderer = NULL;
    SDL_Event event = {0};
    SDL_Color draw_color {0x00, 0x00, 0xFF, 0xFF};
    bool running = true;
};

Game::Game(){};

int Game::init()
{
    bool res = SDL_Init(SDL_INIT_EVERYTHING);
    if(res < 0)
    {
        SDL_Log("Failed to init. (\"%s\").\n", SDL_GetError());
        return res;
    }
    window = SDL_CreateWindow(window_title,
                              SDL_WINDOWPOS_CENTERED,
                              SDL_WINDOWPOS_CENTERED,
                              window_width,
                              window_height,
                              0);
    if(window == NULL)
    {
        SDL_Log("Failed to create a window. (\"%s\").\n", SDL_GetError());
        return -1;
    }

    renderer = SDL_CreateRenderer(window, -1, 0);
    if(renderer == NULL)
    {
        SDL_Log("Failed to create the renderer. (\"%s\").\n", SDL_GetError());
        return -1;
    }
    return 0;
}

void Game::run()
{
    while(running)
    {
        while(SDL_PollEvent(&event))
        {
            if(event.type == SDL_QUIT)
            {
                running = false;
            }
            else if(event.type == SDL_KEYDOWN)
            {
                if(event.key.keysym.sym == SDLK_ESCAPE)
                {
                    running = false;
                }
            }
        }
    }
}

void Game::quit()
{
    if(window)
    {
        SDL_DestroyWindow(window);
    }
    if(renderer)
    {
        SDL_DestroyRenderer(renderer);
    }
    SDL_Quit();
}

int main(int argc, char** argv)
{
    Game game = Game();
    if(game.init() < 0) return 1;
    game.run();
    game.quit();
    return 0;
}
