CC			= gcc
CXX		 	= g++
CFLAGS		= -g -O2 -Wall -fPIC -std=gnu99 
CXXFLAGS	= -g -O2 -Wall -fPIC -std=c++11
CPATH		=
CXXPATH		=
LIBPATH		=
LIBS		=

all: leslie_bin

leslie_bin:
	$(CXX) -o leslie_bin.o -c $(CXXFLAGS) $(CXXPATH) leslie_bin.cpp
	$(CXX) $(LIBPATH) -o leslie_bin leslie_bin.o $(LIBS)

clean: 
	rm -rf *.o leslie_bin
