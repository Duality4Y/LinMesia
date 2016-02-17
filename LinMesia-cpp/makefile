# compiler to use
CC=g++

# flags/options.
CFLAG=-g -Wall


#build dir
BUILDDIR=./build
#include dir
INCDIR=./include
#src dir
SRCDIR=./src
# libraries
# TODO

SOURCES=$(SRCDIR)/*.cpp
OBJECTS=$(SOURCES:.cpp=.o)
EXECUTABLE=LinMesia

$(info VAR is $(SOURCES))
$(info VAR is $(OBJECTS))
$(info VAR is $(BUILDDIR)/$(EXECUTABLE))

all:
	$(CC) $(CFLAGS) $(SOURCES) -o $(BUILDDIR)/$(EXECUTABLE)

clean:
	rm -r $(BUILDDIR)/*