// #include <stdio.h>
// #include <test.h>
// #include "MidiFile.h"

// int main(void)
// {
//     printf("Hello World!\n");
//     print_test();
//     return 0;
// }

#include "MidiFile.h"
#include "Options.h"
#include <iostream>
#include <iomanip>

using namespace std;

int main(int argc, char** argv) {
   Options options;
   options.process(argc, argv);
   MidiFile midifile;
   if (options.getArgCount() > 0) {
      midifile.read(options.getArg(1));
   } else {
      midifile.read(cin);
   }

   int tracks = midifile.getTrackCount();
   cout << "TPQ: " << midifile.getTicksPerQuarterNote() << endl;
   if (tracks > 1) {
      cout << "TRACKS: " << tracks << endl;
   }
   for (int track=0; track < tracks; track++) {
      if (tracks > 1) {
         cout << "\nTrack " << track << endl;
      }
      for (int event=0; event < midifile[track].size(); event++) {
         cout << dec << midifile[track][event].tick;
         cout << '\t' << hex;
         for (int i=0; i<midifile[track][event].size(); i++) {
            cout << (int)midifile[track][event][i] << ' ';
         }
         cout << endl;
      }
   }

   return 0;
}