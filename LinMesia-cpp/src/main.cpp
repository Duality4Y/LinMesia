// #include <stdio.h>
// #include <test.h>
// #include "MidiFile.h"

// int main(void)
// {
//     printf("Hello World!\n");
//     print_test();
//     return 0;
// }

// Example program:
// Using SDL2 to create an application window

#include "SDL.h"
#include <stdio.h>

int main(int argc, char* argv[]) {

    SDL_Window *window;                    // Declare a pointer

    SDL_Init(SDL_INIT_VIDEO);              // Initialize SDL2

    // Create an application window with the following settings:
    window = SDL_CreateWindow(
        "An SDL2 window",                  // window title
        SDL_WINDOWPOS_UNDEFINED,           // initial x position
        SDL_WINDOWPOS_UNDEFINED,           // initial y position
        640,                               // width, in pixels
        480,                               // height, in pixels
        SDL_WINDOW_OPENGL                  // flags - see below
    );

    // Check that the window was successfully created
    if (window == NULL) {
        // In the case that the window could not be made...
        printf("Could not create window: %s\n", SDL_GetError());
        return 1;
    }

    // The window is open: could enter program loop here (see SDL_PollEvent())

    SDL_Delay(3000);  // Pause execution for 3000 milliseconds, for example

    // Close and destroy the window
    SDL_DestroyWindow(window);

    // Clean up
    SDL_Quit();
    return 0;
}


// #include "MidiFile.h"
// #include "Options.h"
// #include <iostream>
// #include <iomanip>

// using namespace std;

// int main(int argc, char** argv) {
//    Options options;
//    options.process(argc, argv);
//    MidiFile midifile;
//    if (options.getArgCount() > 0) {
//       midifile.read(options.getArg(1));
//    } else {
//       midifile.read(cin);
//    }

//    int tracks = midifile.getTrackCount();
//    cout << "TPQ: " << midifile.getTicksPerQuarterNote() << endl;
//    if (tracks > 1) {
//       cout << "TRACKS: " << tracks << endl;
//    }
//    for (int track=0; track < tracks; track++) {
//       if (tracks > 1) {
//          cout << "\nTrack " << track << endl;
//       }
//       for (int event=0; event < midifile[track].size(); event++) {
//          cout << dec << midifile[track][event].tick;
//          cout << '\t' << hex;
//          for (int i=0; i<midifile[track][event].size(); i++) {
//             cout << (int)midifile[track][event][i] << ' ';
//          }
//          cout << endl;
//       }
//    }

//    return 0;
// }