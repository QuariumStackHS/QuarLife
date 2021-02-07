#ifndef ConfigHpp
#define ConfigHpp 1
 #include <iostream>
#include <vector>
#include <string>


using namespace std;
struct QSRObj{
    
};
enum BuildTypes{
    EXE=0,
    OBJ=1,
    Dll=2
};

enum CppVersions{
    CPP11=11,
    CPP17=17
};
class Configurator{
    public:
    Configurator();
    //Data
    string ProgrameName;
    //string *IncPath;
    int buildtype;
    int CPPLang;

};
#endif